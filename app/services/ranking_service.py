"""
Serviço para gerenciar resultados de quiz e ranking
"""
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
from app.models.ranking import ResultadoQuiz, RankingEntry
from app.services.simple_user_service import simple_user_service

try:
    from config.database import get_db_connection
    DB_AVAILABLE = True
except ImportError:
    DB_AVAILABLE = False

class RankingService:
    """Serviço para operações com ranking e resultados"""
    
    def __init__(self):
        self.resultados_memoria = []
        self.proximo_id = 1
    
    def salvar_resultado(self, usuario_id: int, pontuacao: int, total_perguntas: int, 
                        categoria: str, dificuldade: str, tempo_gasto: int = 0) -> ResultadoQuiz:
        """Salva o resultado de um quiz"""
        if DB_AVAILABLE:
            try:
                with get_db_connection() as conn:
                    cursor = conn.cursor(dictionary=True)
                    
                    cursor.execute("""
                        INSERT INTO resultados_quiz 
                        (usuario_id, pontuacao, total_perguntas, categoria, dificuldade, tempo_gasto, data_realizacao)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (usuario_id, pontuacao, total_perguntas, categoria, dificuldade, tempo_gasto, datetime.utcnow()))
                    
                    conn.commit()
                    resultado_id = cursor.lastrowid
                    
                    return ResultadoQuiz(
                        id=resultado_id,
                        usuario_id=usuario_id,
                        pontuacao=pontuacao,
                        total_perguntas=total_perguntas,
                        categoria=categoria,
                        dificuldade=dificuldade,
                        tempo_gasto=tempo_gasto,
                        data_realizacao=datetime.utcnow()
                    )
            except Exception as e:
                print(f"Erro no banco de dados: {e}")
                # Fallback para sistema em memória
                pass
        
        # Sistema em memória (fallback)
        resultado = ResultadoQuiz(
            id=self.proximo_id,
            usuario_id=usuario_id,
            pontuacao=pontuacao,
            total_perguntas=total_perguntas,
            categoria=categoria,
            dificuldade=dificuldade,
            tempo_gasto=tempo_gasto,
            data_realizacao=datetime.utcnow()
        )
        
        self.resultados_memoria.append(resultado)
        self.proximo_id += 1
        
        return resultado
    
    def obter_ranking_geral(self, limite: int = 50) -> List[RankingEntry]:
        """Obtém o ranking geral dos usuários"""
        if DB_AVAILABLE:
            try:
                with get_db_connection() as conn:
                    cursor = conn.cursor(dictionary=True)
                    
                    cursor.execute("""
                        SELECT 
                            r.usuario_id,
                            u.nome as nome_usuario,
                            SUM(r.pontuacao) as pontuacao_total,
                            COUNT(r.id) as total_quizes,
                            MAX(r.pontuacao) as melhor_pontuacao,
                            (
                                SELECT categoria 
                                FROM resultados_quiz r2 
                                WHERE r2.usuario_id = r.usuario_id 
                                GROUP BY categoria 
                                ORDER BY COUNT(*) DESC 
                                LIMIT 1
                            ) as categoria_preferida
                        FROM resultados_quiz r
                        JOIN usuarios u ON r.usuario_id = u.id
                        WHERE u.ativo = TRUE
                        GROUP BY r.usuario_id, u.nome
                        ORDER BY pontuacao_total DESC, melhor_pontuacao DESC
                        LIMIT %s
                    """, (limite,))
                    
                    resultados = cursor.fetchall()
                    
                    ranking = []
                    for r in resultados:
                        entry = RankingEntry(
                            usuario_id=r['usuario_id'],
                            nome_usuario=r['nome_usuario'],
                            pontuacao_total=r['pontuacao_total'],
                            total_quizes=r['total_quizes'],
                            melhor_pontuacao=r['melhor_pontuacao'],
                            categoria_preferida=r['categoria_preferida'] or 'geral'
                        )
                        ranking.append(entry)
                    
                    return ranking
            except Exception as e:
                print(f"Erro no banco de dados: {e}")
                # Fallback para sistema em memória
                pass
        
        # Sistema em memória (fallback)
        return self._calcular_ranking_memoria(limite)
    
    def obter_ranking_categoria(self, categoria: str, limite: int = 50) -> List[RankingEntry]:
        """Obtém o ranking por categoria específica"""
        if DB_AVAILABLE:
            try:
                with get_db_connection() as conn:
                    cursor = conn.cursor(dictionary=True)
                    
                    cursor.execute("""
                        SELECT 
                            r.usuario_id,
                            u.nome as nome_usuario,
                            SUM(r.pontuacao) as pontuacao_total,
                            COUNT(r.id) as total_quizes,
                            MAX(r.pontuacao) as melhor_pontuacao,
                            %s as categoria_preferida
                        FROM resultados_quiz r
                        JOIN usuarios u ON r.usuario_id = u.id
                        WHERE u.ativo = TRUE AND r.categoria = %s
                        GROUP BY r.usuario_id, u.nome
                        ORDER BY pontuacao_total DESC, melhor_pontuacao DESC
                        LIMIT %s
                    """, (categoria, categoria, limite))
                    
                    resultados = cursor.fetchall()
                    
                    ranking = []
                    for r in resultados:
                        entry = RankingEntry(
                            usuario_id=r['usuario_id'],
                            nome_usuario=r['nome_usuario'],
                            pontuacao_total=r['pontuacao_total'],
                            total_quizes=r['total_quizes'],
                            melhor_pontuacao=r['melhor_pontuacao'],
                            categoria_preferida=categoria
                        )
                        ranking.append(entry)
                    
                    return ranking
            except Exception as e:
                print(f"Erro no banco de dados: {e}")
                # Fallback para sistema em memória
                pass
        
        # Sistema em memória (fallback)
        return self._calcular_ranking_memoria_categoria(categoria, limite)
    
    def obter_estatisticas_usuario(self, usuario_id: int) -> Dict[str, Any]:
        """Obtém estatísticas detalhadas de um usuário"""
        if DB_AVAILABLE:
            try:
                with get_db_connection() as conn:
                    cursor = conn.cursor(dictionary=True)
                    
                    # Estatísticas gerais
                    cursor.execute("""
                        SELECT 
                            COUNT(*) as total_quizes,
                            SUM(pontuacao) as pontuacao_total,
                            AVG(pontuacao) as media_pontuacao,
                            MAX(pontuacao) as melhor_pontuacao,
                            MIN(pontuacao) as pior_pontuacao,
                            SUM(total_perguntas) as total_perguntas_respondidas
                        FROM resultados_quiz 
                        WHERE usuario_id = %s
                    """, (usuario_id,))
                    
                    stats_gerais = cursor.fetchone()
                    
                    # Estatísticas por categoria
                    cursor.execute("""
                        SELECT 
                            categoria,
                            COUNT(*) as total_quizes,
                            SUM(pontuacao) as pontuacao_total,
                            AVG(pontuacao) as media_pontuacao,
                            MAX(pontuacao) as melhor_pontuacao
                        FROM resultados_quiz 
                        WHERE usuario_id = %s
                        GROUP BY categoria
                        ORDER BY total_quizes DESC
                    """, (usuario_id,))
                    
                    stats_categorias = cursor.fetchall()
                    
                    # Estatísticas por dificuldade
                    cursor.execute("""
                        SELECT 
                            dificuldade,
                            COUNT(*) as total_quizes,
                            SUM(pontuacao) as pontuacao_total,
                            AVG(pontuacao) as media_pontuacao,
                            MAX(pontuacao) as melhor_pontuacao
                        FROM resultados_quiz 
                        WHERE usuario_id = %s
                        GROUP BY dificuldade
                        ORDER BY total_quizes DESC
                    """, (usuario_id,))
                    
                    stats_dificuldades = cursor.fetchall()
                    
                    return {
                        'usuario_id': usuario_id,
                        'estatisticas_gerais': stats_gerais,
                        'estatisticas_categorias': stats_categorias,
                        'estatisticas_dificuldades': stats_dificuldades
                    }
            except Exception as e:
                print(f"Erro no banco de dados: {e}")
                # Fallback para sistema em memória
                pass
        
        # Sistema em memória (fallback)
        return self._calcular_estatisticas_memoria(usuario_id)
    
    def _calcular_ranking_memoria(self, limite: int) -> List[RankingEntry]:
        """Calcula ranking usando dados em memória"""
        # Agrupar resultados por usuário
        resultados_por_usuario = {}
        
        for resultado in self.resultados_memoria:
            if resultado.usuario_id not in resultados_por_usuario:
                resultados_por_usuario[resultado.usuario_id] = []
            resultados_por_usuario[resultado.usuario_id].append(resultado)
        
        # Calcular ranking
        ranking = []
        for usuario_id, resultados in resultados_por_usuario.items():
            try:
                usuario = simple_user_service.get_user_by_id(usuario_id)
                if not usuario:
                    continue
                
                pontuacao_total = sum(r.pontuacao for r in resultados)
                total_quizes = len(resultados)
                melhor_pontuacao = max(r.pontuacao for r in resultados)
                
                # Categoria preferida (mais jogada)
                categorias = [r.categoria for r in resultados]
                categoria_preferida = max(set(categorias), key=categorias.count)
                
                entry = RankingEntry(
                    usuario_id=usuario_id,
                    nome_usuario=usuario.nome,
                    pontuacao_total=pontuacao_total,
                    total_quizes=total_quizes,
                    melhor_pontuacao=melhor_pontuacao,
                    categoria_preferida=categoria_preferida
                )
                ranking.append(entry)
            except Exception as e:
                print(f"Erro ao processar usuário {usuario_id}: {e}")
                continue
        
        # Ordenar por pontuação total
        ranking.sort(key=lambda x: (x.pontuacao_total, x.melhor_pontuacao), reverse=True)
        
        return ranking[:limite]
    
    def _calcular_ranking_memoria_categoria(self, categoria: str, limite: int) -> List[RankingEntry]:
        """Calcula ranking por categoria usando dados em memória"""
        # Filtrar resultados por categoria
        resultados_categoria = [r for r in self.resultados_memoria if r.categoria == categoria]
        
        # Agrupar por usuário
        resultados_por_usuario = {}
        for resultado in resultados_categoria:
            if resultado.usuario_id not in resultados_por_usuario:
                resultados_por_usuario[resultado.usuario_id] = []
            resultados_por_usuario[resultado.usuario_id].append(resultado)
        
        # Calcular ranking
        ranking = []
        for usuario_id, resultados in resultados_por_usuario.items():
            try:
                usuario = simple_user_service.get_user_by_id(usuario_id)
                if not usuario:
                    continue
                
                pontuacao_total = sum(r.pontuacao for r in resultados)
                total_quizes = len(resultados)
                melhor_pontuacao = max(r.pontuacao for r in resultados)
                
                entry = RankingEntry(
                    usuario_id=usuario_id,
                    nome_usuario=usuario.nome,
                    pontuacao_total=pontuacao_total,
                    total_quizes=total_quizes,
                    melhor_pontuacao=melhor_pontuacao,
                    categoria_preferida=categoria
                )
                ranking.append(entry)
            except Exception as e:
                print(f"Erro ao processar usuário {usuario_id}: {e}")
                continue
        
        # Ordenar por pontuação total
        ranking.sort(key=lambda x: (x.pontuacao_total, x.melhor_pontuacao), reverse=True)
        
        return ranking[:limite]
    
    def _calcular_estatisticas_memoria(self, usuario_id: int) -> Dict[str, Any]:
        """Calcula estatísticas usando dados em memória"""
        resultados_usuario = [r for r in self.resultados_memoria if r.usuario_id == usuario_id]
        
        if not resultados_usuario:
            return {
                'usuario_id': usuario_id,
                'estatisticas_gerais': {
                    'total_quizes': 0,
                    'pontuacao_total': 0,
                    'media_pontuacao': 0,
                    'melhor_pontuacao': 0,
                    'pior_pontuacao': 0,
                    'total_perguntas_respondidas': 0
                },
                'estatisticas_categorias': [],
                'estatisticas_dificuldades': []
            }
        
        # Estatísticas gerais
        total_quizes = len(resultados_usuario)
        pontuacao_total = sum(r.pontuacao for r in resultados_usuario)
        media_pontuacao = pontuacao_total / total_quizes if total_quizes > 0 else 0
        melhor_pontuacao = max(r.pontuacao for r in resultados_usuario)
        pior_pontuacao = min(r.pontuacao for r in resultados_usuario)
        total_perguntas_respondidas = sum(r.total_perguntas for r in resultados_usuario)
        
        stats_gerais = {
            'total_quizes': total_quizes,
            'pontuacao_total': pontuacao_total,
            'media_pontuacao': round(media_pontuacao, 2),
            'melhor_pontuacao': melhor_pontuacao,
            'pior_pontuacao': pior_pontuacao,
            'total_perguntas_respondidas': total_perguntas_respondidas
        }
        
        # Estatísticas por categoria
        categorias = {}
        for resultado in resultados_usuario:
            if resultado.categoria not in categorias:
                categorias[resultado.categoria] = []
            categorias[resultado.categoria].append(resultado)
        
        stats_categorias = []
        for categoria, resultados in categorias.items():
            stats_categorias.append({
                'categoria': categoria,
                'total_quizes': len(resultados),
                'pontuacao_total': sum(r.pontuacao for r in resultados),
                'media_pontuacao': round(sum(r.pontuacao for r in resultados) / len(resultados), 2),
                'melhor_pontuacao': max(r.pontuacao for r in resultados)
            })
        
        # Estatísticas por dificuldade
        dificuldades = {}
        for resultado in resultados_usuario:
            if resultado.dificuldade not in dificuldades:
                dificuldades[resultado.dificuldade] = []
            dificuldades[resultado.dificuldade].append(resultado)
        
        stats_dificuldades = []
        for dificuldade, resultados in dificuldades.items():
            stats_dificuldades.append({
                'dificuldade': dificuldade,
                'total_quizes': len(resultados),
                'pontuacao_total': sum(r.pontuacao for r in resultados),
                'media_pontuacao': round(sum(r.pontuacao for r in resultados) / len(resultados), 2),
                'melhor_pontuacao': max(r.pontuacao for r in resultados)
            })
        
        return {
            'usuario_id': usuario_id,
            'estatisticas_gerais': stats_gerais,
            'estatisticas_categorias': stats_categorias,
            'estatisticas_dificuldades': stats_dificuldades
        }

# Instância global do serviço de ranking
ranking_service = RankingService()

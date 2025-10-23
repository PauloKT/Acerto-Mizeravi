"""
Rotas para sistema de ranking e resultados
"""
from flask import Blueprint, request, jsonify
from app.services.ranking_service import ranking_service

ranking_bp = Blueprint('ranking', __name__)

@ranking_bp.route('/api/ranking/geral', methods=['GET'])
def obter_ranking_geral():
    """Obtém o ranking geral dos usuários"""
    try:
        limite = request.args.get('limite', 50, type=int)
        limite = min(limite, 100)  # Limitar a 100 para evitar sobrecarga
        
        ranking = ranking_service.obter_ranking_geral(limite)
        
        return jsonify({
            'sucesso': True,
            'ranking': [entry.to_dict() for entry in ranking],
            'total': len(ranking)
        })
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro interno: {str(e)}'}), 500

@ranking_bp.route('/api/ranking/categoria/<categoria>', methods=['GET'])
def obter_ranking_categoria(categoria):
    """Obtém o ranking por categoria específica"""
    try:
        limite = request.args.get('limite', 50, type=int)
        limite = min(limite, 100)  # Limitar a 100 para evitar sobrecarga
        
        ranking = ranking_service.obter_ranking_categoria(categoria, limite)
        
        return jsonify({
            'sucesso': True,
            'categoria': categoria,
            'ranking': [entry.to_dict() for entry in ranking],
            'total': len(ranking)
        })
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro interno: {str(e)}'}), 500

@ranking_bp.route('/api/ranking/estatisticas/<int:usuario_id>', methods=['GET'])
def obter_estatisticas_usuario(usuario_id):
    """Obtém estatísticas detalhadas de um usuário"""
    try:
        estatisticas = ranking_service.obter_estatisticas_usuario(usuario_id)
        
        return jsonify({
            'sucesso': True,
            'estatisticas': estatisticas
        })
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro interno: {str(e)}'}), 500

@ranking_bp.route('/api/ranking/salvar-resultado', methods=['POST'])
def salvar_resultado():
    """Salva o resultado de um quiz"""
    try:
        data = request.get_json()
        
        # Validar dados obrigatórios
        campos_obrigatorios = ['usuario_id', 'pontuacao', 'total_perguntas', 'categoria', 'dificuldade']
        for campo in campos_obrigatorios:
            if campo not in data:
                return jsonify({'sucesso': False, 'erro': f'Campo obrigatório: {campo}'}), 400
        
        # Validar tipos
        try:
            usuario_id = int(data['usuario_id'])
            pontuacao = int(data['pontuacao'])
            total_perguntas = int(data['total_perguntas'])
            tempo_gasto = int(data.get('tempo_gasto', 0))
        except (ValueError, TypeError):
            return jsonify({'sucesso': False, 'erro': 'Dados inválidos'}), 400
        
        # Validar valores
        if pontuacao < 0 or total_perguntas <= 0 or pontuacao > total_perguntas:
            return jsonify({'sucesso': False, 'erro': 'Valores inválidos'}), 400
        
        categoria = data['categoria'].strip()
        dificuldade = data['dificuldade'].strip()
        
        if not categoria or not dificuldade:
            return jsonify({'sucesso': False, 'erro': 'Categoria e dificuldade são obrigatórios'}), 400
        
        # Salvar resultado
        resultado = ranking_service.salvar_resultado(
            usuario_id=usuario_id,
            pontuacao=pontuacao,
            total_perguntas=total_perguntas,
            categoria=categoria,
            dificuldade=dificuldade,
            tempo_gasto=tempo_gasto
        )
        
        return jsonify({
            'sucesso': True,
            'mensagem': 'Resultado salvo com sucesso',
            'resultado': resultado.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro interno: {str(e)}'}), 500

@ranking_bp.route('/api/ranking/categorias', methods=['GET'])
def obter_categorias_ranking():
    """Obtém as categorias disponíveis para ranking"""
    try:
        categorias = ['geral', 'humanas', 'exatas', 'biologicas', 'geografia', 'historia', 'tecnologia']
        
        return jsonify({
            'sucesso': True,
            'categorias': categorias
        })
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro interno: {str(e)}'}), 500

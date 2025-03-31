def get_career_recommendation(hardware_info):
    """
    Determina una carrera recomendada basada en las especificaciones del hardware
    """
    scores = {
        'cpu': 0,
        'ram': 0,
        'disk': 0,
        'gpu': 0
    }
    
    # Evaluar CPU
    try:
        cores = hardware_info['cpu']['cores_total']
        if cores >= 16:
            scores['cpu'] = 5
        elif cores >= 8:
            scores['cpu'] = 4
        elif cores >= 4:
            scores['cpu'] = 3
        elif cores >= 2:
            scores['cpu'] = 2
        else:
            scores['cpu'] = 1
    except Exception:
        scores['cpu'] = 1
    
    # Evaluar RAM
    try:
        ram_mb = hardware_info['ram']['total_mb']
        if ram_mb >= 32768:  # 32 GB
            scores['ram'] = 5
        elif ram_mb >= 16384:  # 16 GB
            scores['ram'] = 4
        elif ram_mb >= 8192:  # 8 GB
            scores['ram'] = 3
        elif ram_mb >= 4096:  # 4 GB
            scores['ram'] = 2
        else:
            scores['ram'] = 1
    except Exception:
        scores['ram'] = 1
    
    # Evaluar Disco
    try:
        disk_gb = hardware_info['disk']['total_gb']
        if disk_gb >= 2048:  # 2 TB
            scores['disk'] = 5
        elif disk_gb >= 1024:  # 1 TB
            scores['disk'] = 4
        elif disk_gb >= 512:  # 512 GB
            scores['disk'] = 3
        elif disk_gb >= 256:  # 256 GB
            scores['disk'] = 2
        else:
            scores['disk'] = 1
    except Exception:
        scores['disk'] = 1
    
    # Evaluar GPU
    try:
        gpu_info = hardware_info['gpu'][0]
        if 'error' in gpu_info or 'No dedicated GPU' in gpu_info.get('name', ''):
            scores['gpu'] = 1
        else:
            gpu_name = gpu_info.get('name', '').lower()
            
            # Detectar tarjetas de gama alta
            if any(high_end in gpu_name for high_end in ['rtx', 'titan', 'radeon vii', 'rx 6800', 'rx 6900', 'quadro']):
                scores['gpu'] = 5
            # Detectar tarjetas de gama media-alta
            elif any(mid_high in gpu_name for mid_high in ['gtx 1080', 'gtx 1070', 'rtx 2060', 'rtx 3060', 'rx 5700']):
                scores['gpu'] = 4
            # Detectar tarjetas de gama media
            elif any(mid in gpu_name for mid in ['gtx 1060', 'gtx 1650', 'rx 580', 'rx 590']):
                scores['gpu'] = 3
            # Detectar tarjetas de gama baja
            elif any(low in gpu_name for low in ['gtx 1050', 'gtx 1030', 'mx', 'rx 560', 'rx 550']):
                scores['gpu'] = 2
            else:
                scores['gpu'] = 1
    except Exception:
        scores['gpu'] = 1
    
    # Calcular puntuación total (ponderada)
    total_score = (scores['cpu'] * 0.3) + (scores['ram'] * 0.3) + (scores['disk'] * 0.1) + (scores['gpu'] * 0.3)
    
    # Definir carreras y mensajes humorísticos según puntuación
    careers = [
        {
            'score_range': (4.5, 5.0),
            'career': "Ingeniero de IA / Científico de Datos",
            'description': "¡Felicidades! Con ese hardware podrías entrenar la próxima IA que nos reemplazará a todos. Tu computadora es más inteligente que muchos humanos.",
            'salary': "$100,000 - $150,000",
            'emoji': "🤖"
        },
        {
            'score_range': (4.0, 4.49),
            'career': "Desarrollador de Videojuegos",
            'description': "Tu máquina es capaz de hacer llorar a los gráficos más exigentes. Podrías crear el próximo Cyberpunk 2077, ¡pero que funcione correctamente!",
            'salary': "$80,000 - $120,000",
            'emoji': "🎮"
        },
        {
            'score_range': (3.5, 3.99),
            'career': "Ingeniero de Software / Desarrollador Full-Stack",
            'description': "Tienes un buen equipo para programar y ejecutar varios entornos de desarrollo a la vez. Visual Studio, Docker y 500 pestañas de Stack Overflow no te asustan.",
            'salary': "$70,000 - $110,000",
            'emoji': "💻"
        },
        {
            'score_range': (3.0, 3.49),
            'career': "Diseñador Gráfico / Editor de Video",
            'description': "Adobe Creative Suite funcionará bien en tu equipo. Puedes hacer que las cosas se vean bonitas, pero no esperes renderizar la próxima película de Pixar.",
            'salary': "$50,000 - $80,000",
            'emoji': "🎨"
        },
        {
            'score_range': (2.5, 2.99),
            'career': "Analista de Datos / Gerente de Proyecto",
            'description': "Excel, PowerBI y algunas videollamadas simultáneas de Microsoft Teams no serán problema. Tu hardware es el equivalente a un gerente de nivel medio: nada especial pero hace el trabajo.",
            'salary': "$60,000 - $90,000",
            'emoji': "📊"
        },
        {
            'score_range': (2.0, 2.49),
            'career': "Técnico de Soporte IT / Administrador de Sistemas",
            'description': "Tu equipo es básico pero funcional, como tu futuro trabajo diciéndole a la gente que reinicie su computadora. '¿Ha probado apagarlo y volverlo a encender?'",
            'salary': "$45,000 - $65,000",
            'emoji': "🔧"
        },
        {
            'score_range': (1.5, 1.99),
            'career': "Asistente Administrativo / Operador de Entrada de Datos",
            'description': "Tu computadora puede ejecutar Microsoft Office... la mayor parte del tiempo. Es perfecta para escribir correos electrónicos y documentos, justo como tu futuro trabajo.",
            'salary': "$35,000 - $45,000",
            'emoji': "📝"
        },
        {
            'score_range': (1.0, 1.49),
            'career': "Barrendero Digital / Influencer de MySpace",
            'description': "¿Tu computadora a veces emite ruidos extraños y huele a quemado? ¡Felicidades! Estás calificado para limpiar archivos temporales o intentar revivir plataformas sociales obsoletas desde un cibercafé.",
            'salary': "$15,000 - $25,000",
            'emoji': "🧹"
        },
        {
            'score_range': (0, 0.99),
            'career': "Filosofía de la Tecnología / Monje Digital",
            'description': "Tu hardware es tan antiguo que podrías argumentar que no existe. Perfecta para reflexionar sobre la naturaleza efímera de la tecnología mientras esperas que se abra una página web.",
            'salary': "Paz interior y enlightenment",
            'emoji': "🧘‍♂️"
        }
    ]
    
    # Encontrar la carrera adecuada según la puntuación
    recommended_career = None
    for career in careers:
        if career['score_range'][0] <= total_score <= career['score_range'][1]:
            recommended_career = career
            break
    
    # Si por alguna razón no encontramos una carrera adecuada, usar la más baja
    if not recommended_career:
        recommended_career = careers[-1]
    
    # Agregar puntuaciones y hardware score
    result = {
        'recommendation': recommended_career,
        'hardware_scores': scores,
        'total_score': total_score,
        'hardware_rating': f"{total_score:.1f}/5.0"
    }
    
    return result
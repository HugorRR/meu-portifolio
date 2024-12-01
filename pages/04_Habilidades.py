import streamlit as st

def habilidades():
    st.set_page_config(page_title="Portfólio de Habilidades", page_icon="🚀", layout="wide")
    
    st.markdown("""
    <style>
    /* Estilo de fundo e tipografia */
    body {
        background-color: #f4f6f9;
        font-family: 'Inter', sans-serif;
    }

    /* Contêiner principal */
    .main-container {
        background: linear-gradient(135deg, #ffffff 0%, #f1f3f6 100%);
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }

    /* Cabeçalho */
    .skill-section-title {
        text-align: center;
        color: #2c3e50;
        font-size: 2.5em;
        margin-bottom: 30px;
        font-weight: 700;
        background: linear-gradient(to right, #3498db, #2ecc71);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Cartões de Habilidades */
    .skill-card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
    }

    .skill-card:hover {
        transform: scale(1.03);
    }

    /* Barras de Progresso */
    .skill-progress-container {
        background-color: #e9ecef;
        border-radius: 10px;
        height: 15px;
        overflow: hidden;
    }

    .skill-progress {
        background: linear-gradient(to right, #3498db, #2ecc71);
        height: 100%;
        border-radius: 10px;
        transition: width 1s ease-in-out;
    }

    /* Badges de Habilidades */
    .skill-badge {
        display: inline-block;
        background-color: #3498db;
        color: white;
        padding: 8px 15px;
        margin: 5px;
        border-radius: 20px;
        font-size: 0.9em;
        transition: background-color 0.3s ease;
    }

    .skill-badge:hover {
        background-color: #2980b9;
    }

    .creative-badge {
        background-color: #e74c3c;
    }

    .creative-badge:hover {
        background-color: #c0392b;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="skill-section-title">🚀 Minhas Habilidades Profissionais</h1>', unsafe_allow_html=True)

    habilidades_tecnicas = [
        {"nome": "Python", "nivel": 85},
        {"nome": "Automação", "nivel": 90},
        {"nome": "Suporte Técnico", "nivel": 80},
        {"nome": "Web Scraping", "nivel": 90},
        {"nome": "Análise de Sistemas", "nivel": 75},
        {"nome": "Resolução de Problemas", "nivel": 85},
    ]

    habilidades_interpessoais = [
        "Comunicação", 
        "Trabalho em Equipe", 
        "Resolução de Problemas", 
        "Adaptabilidade", 
        "Liderança"
    ]

    habilidades_criativas = [
        "Design Gráfico",
        "Criação de Logos", 
        "Ilustração Digital", 
        "Arte Digital", 
        "Photoshop",
        "Edição de Imagens"
    ]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<h3 style="color:#3498db;">💻 Habilidades Técnicas</h3>', unsafe_allow_html=True)
        
        for skill in habilidades_tecnicas:
            st.markdown(f"""
            <div style="margin-bottom: 15px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <span>{skill['nome']}</span>
                    <span>{skill['nivel']}%</span>
                </div>
                <div class="skill-progress-container">
                    <div class="skill-progress" style="width:{skill['nivel']}%"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<h3 style="color:#2ecc71;">🤝 Habilidades Interpessoais</h3>', unsafe_allow_html=True)
        
        for skill in habilidades_interpessoais:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<h3 style="color:#e74c3c;">🎨 Habilidades Criativas</h3>', unsafe_allow_html=True)
        
        for skill in habilidades_criativas:
            st.markdown(f'<span class="skill-badge creative-badge">{skill}</span>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("## Minha Abordagem Profissional")
    st.markdown("""
    Combino habilidades técnicas precisas com criatividade para desenvolver 
    soluções inovadoras. Minha formação multidisciplinar me permite abordar 
    desafios de forma holística, integrando tecnologia e design.

    ### Diferencial
    - 🔍 Capacidade de traduzir ideias complexas em soluções práticas
    - 🌱 Aprendizado contínuo e adaptabilidade
    - 🎯 Foco em resultados que agregam valor
    """)

def main():
    habilidades()

if __name__ == "__main__":
    main()
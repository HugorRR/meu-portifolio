import streamlit as st
import streamlit.components.v1 as components

def educacao():
    st.set_page_config(page_title="Educação", layout="wide", page_icon="👨‍🎓")

    st.markdown("""
    <style>
    .title {
        font-size: 2.5em;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
        font-weight: bold;
    }
    .education-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    .education-card:hover {
        transform: scale(1.02);
    }
    .education-title {
        color: #2980b9;
        margin-bottom: 10px;
    }
    .education-details {
        color: #34495e;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="title">📚 Formação Acadêmica e Certificações</h1>', unsafe_allow_html=True)

    educacoes = [
        {
            "titulo": "Analise e Desenvolvimento de Sistemas",
            "instituicao": "Universidade de Marilia",
            "periodo": "2022 - 2025",
            "status": "Cursando",
            "destaque": True
        },
        {
            "titulo": "Administração",
            "instituicao": "Anhanguera FAC-4",
            "periodo": "2018 - 2021",
            "status": "Incompleto",
            "destaque": False
        }
    ]

    certificacoes = [
        {
            "titulo": "Trilha de Aprendizado em Python",
            "instituicao": "Asimov",
            "carga_horaria": "22h",
            "conclusao": "06/2024"
        },
        {
            "titulo": "Trilha de Aprendizado em Aplicações IA com Python",
            "instituicao": "Asimov",
            "carga_horaria": "50.5h",
            "conclusao": "06/2024"
        },
        {
            "titulo": "Trilha de Aprendizado em Python Office",
            "instituicao": "Asimov",
            "carga_horaria": "47.5h",
            "conclusao": "06/2024"
        },
        {
            "titulo": "Desenvolvimento de Aplicativos na Plataforma AppSheet",
            "instituicao": "Udemy",
            "carga_horaria": "20h",
            "conclusao": "01/2023"
        }
    ]

    st.markdown('<h2 class="education-title">🎓 Formação Acadêmica</h2>', unsafe_allow_html=True)
    
    for educacao in educacoes:
        st.markdown(f"""
        <div class="education-card">
            <h3 class="education-title">{educacao['titulo']}</h3>
            <p class="education-details">
            <strong>Instituição:</strong> {educacao['instituicao']}<br>
            <strong>Período:</strong> {educacao['periodo']}<br>
            <strong>Status:</strong> {educacao['status']}
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<h2 class="education-title">🏆 Certificações e Cursos</h2>', unsafe_allow_html=True)
    
    for certificacao in certificacoes:
        st.markdown(f"""
        <div class="education-card">
            <h3 class="education-title">{certificacao['titulo']}</h3>
            <p class="education-details">
            <strong>Instituição:</strong> {certificacao['instituicao']}<br>
            <strong>Carga Horária:</strong> {certificacao['carga_horaria']}<br>
            <strong>Conclusão:</strong> {certificacao['conclusao']}
            </p>
        </div>
        """, unsafe_allow_html=True)

def main():
    educacao()

if __name__ == "__main__":
    main()
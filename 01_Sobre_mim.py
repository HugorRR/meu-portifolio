import streamlit as st
from PIL import Image

def sobre():
    st.set_page_config(page_title="Sobre", layout="wide", page_icon="🙋🏻")

    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("Hugo Rogério Néri Laurentino")
        st.subheader("Analista de T.I | Designer Criativo")

    with col2:
        minha_foto = r"minha_foto.png"
        st.image(minha_foto, width=200, use_column_width=False)

    st.markdown("---")

    st.markdown("## Sobre Mim")
    
    st.markdown("""
    Sou um profissional apaixonado por tecnologia e criatividade, com uma abordagem 
    multidisciplinar que busca constantemente inovar e resolver desafios complexos.

    Minha trajetória é marcada pela capacidade de integrar conhecimentos técnicos 
    com soluções criativas, sempre com foco em resultados eficientes e impactantes.

    Atualmente, trabalho como Analista de TI Junior, onde aplico meus conhecimentos 
    em desenvolvimento de software, suporte técnico e design.
    """)

    st.markdown("### Minha Filosofia")
    st.markdown("""
    - 🚀 Aprendizado contínuo e adaptabilidade
    - 🤝 Colaboração e trabalho em equipe
    - 💡 Pensamento crítico e solução de problemas
    - 🎨 Criatividade como diferencial competitivo
    """)

def contato():
    st.header("Contato")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("### 📧 Email")
        st.write("hugorogerio522@gmail.com")
    
    with col2:
        st.markdown("### 🔗 LinkedIn")
        st.markdown("[Conecte-se no LinkedIn](https://www.linkedin.com/in/hugo-neri-855a95228/)")
    
    with col3:
        st.markdown("### 💻 GitHub")
        st.markdown("[Veja meus projetos](https://github.com/HugorRR)")
    
def main():
    sobre()
    contato()

if __name__ == "__main__":
    main()
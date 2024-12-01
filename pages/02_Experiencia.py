import streamlit as st

def experiencia():
    st.set_page_config(page_title="Experiencia", layout="wide", page_icon="💼")
    
    st.markdown("<h1 style='text-align: center; color: #2C3E50;'>Experiência Profissional</h1>", unsafe_allow_html=True)
    
    def criar_cartao_experiencia(cargo, empresa, periodo, local, descricoes, tecnologias=None):
        descricao_formatada = "\n".join([f"• {desc}" for desc in descricoes])
        
        tecnologias_formatadas = f"<div style='margin-top: 10px; color: #34495E;'><strong>Principais Tecnologias:</strong> {', '.join(tecnologias)}</div>" if tecnologias else ''
        
        st.markdown(f"""
        <div style='
            background-color: #F4F6F7; 
            border-radius: 10px; 
            padding: 20px; 
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border-left: 5px solid #3498DB;
        '>
            <h3 style='color: #2C3E50; margin-bottom: 5px;'>{cargo}</h3>
            <p style='color: #7F8C8D; margin-bottom: 10px;'>
                <strong>{empresa}</strong> | {periodo}
            </p>
            <p style='color: #7F8C8D; margin-bottom: 10px;'>
                📍 {local}
            </p>
            <div style='color: #34495E; white-space: pre-wrap;'>{descricao_formatada}</div>
            {tecnologias_formatadas}
        """, unsafe_allow_html=True)

    criar_cartao_experiencia(
        cargo="Analista de TI Junior",
        empresa="B/Palma Contabilidade",
        periodo="10/2023 - Presente",
        local="Local não especificado",
        descricoes=[
            "Suporte técnico proativo para sistemas internos",
            "Desenvolvimento de aplicações personalizadas com AppSheet", 
            "Implementação de automações em Python",
            "Realização de web scraping para otimização de processos", 
            "Manutenção preventiva e corretiva de recursos de TI",
            "Atendimento direto ao cliente, garantindo experiência positiva"
        ],
        tecnologias=[
            "Python", 
            "AppSheet", 
            "Web Scraping", 
            "Automação", 
            "Suporte Técnico"
        ]
    )

    criar_cartao_experiencia(
        cargo="Auxiliar Administrativo",
        empresa="B/Palma Contabilidade",
        periodo="03/2021 - 10/2023",
        local="Local não especificado",
        descricoes=[
            "Suporte técnico para sistemas internos",
            "Atendimento ao cliente e resolução de problemas", 
            "Manutenção de computadores e recursos de TI",
            "Apoio em processos administrativos",
            "Organização e gestão de documentos"
        ],
        tecnologias=[
            "Suporte Técnico", 
            "Atendimento ao Cliente", 
            "Manutenção de Computadores"
        ]
    )

    criar_cartao_experiencia(
        cargo="Auxiliar de Escritório em Geral",
        empresa="Rede Parmeggio",
        periodo="Nov 2019 - Out 2020 · 1 ano",
        local="Campinas, São Paulo, Brasil",
        descricoes=[
            "Realizava atendimento ao cliente",
            "Controle de estoque",
            "Controle de notas fiscais",
            "Organização e arquivamento de documentos"
        ]
    )

    criar_cartao_experiencia(
        cargo="Operador de Telemarketing",
        empresa="Telemabi",
        periodo="Mar 2017 - Out 2017 · 8 meses",
        local="Campinas, São Paulo, Brasil",
        descricoes=[
            "Realizava atendimento ao cliente via telefone",
            "Prestava suporte e informações sobre produtos e serviços",
            "Registro e acompanhamento de chamados",
            "Cumprimento de metas de atendimento e satisfação do cliente"
        ]
    )

    criar_cartao_experiencia(
        cargo="Auxiliar de Escritório",
        empresa="Instituto de Química - Unicamp",
        periodo="Jun 2014 - Abr 2015 · 11 meses",
        local="Campinas, São Paulo, Brasil",
        descricoes=[
            "Organização de estoque e expedição de malotes",
            "Suporte administrativo em departamento acadêmico",
            "Controle e registro de documentos e materiais",
            "Auxílio em processos internos do instituto"
        ]
    )

def main():
    experiencia()

if __name__ == "__main__":
    main()
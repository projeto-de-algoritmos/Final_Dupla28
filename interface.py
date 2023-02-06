import streamlit as st
import huffman_code

#Title
st.title('Trabalho final - Dupla 28')
st.write('Huffman Encoding')


st.subheader("O que deseja fazer?")
opcao = st.radio("", ("Compactar", "Descompactar"))

st.subheader("Selecione um arquivo para compactar")
uploaded_file = st.file_uploader("Escolha  seu arquivo .txt", type=["txt"])

if uploaded_file:
    if opcao == "Compactar":
        # To convert to a string based IO:
        stringio = str(uploaded_file.getvalue().decode("utf-8"))

        # Cria um arquivo nesse diretorio com conteúdo do arquivo original
        with open(uploaded_file.name, 'w') as f:
            f.write(stringio)

        file = huffman_code.compress(uploaded_file.name)
        #name = uploaded_file.name.rsplit(".", 1)
        #name[-1] = "sl28"
        #new_filename = "_".join(name)
        # Adicionar uma opção para baixar o arquivo modificado
        st.markdown("""
        Para baixar o arquivo modificado, clique no botão abaixo:

        """)
        st.markdown("""
        <a href="data:text/plain;charset=utf-8,{}" download="compacted_file.sl28">
        Baixa arquivo compactado
        </a>
        """.format(file), unsafe_allow_html=True)
        
    else:
        pass
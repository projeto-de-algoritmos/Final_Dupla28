import streamlit as st
import huffman_code

#Title
st.title('Trabalho final - Dupla 28')
st.write('Huffman Encoding')


st.subheader("O que deseja fazer?")
opcao = st.radio("", ("Compactar", "Descompactar"))

st.subheader("Selecione um arquivo para compactar")
uploaded_file = st.file_uploader("Escolha  seu arquivo .txt", type=["txt", "slt28"])

if uploaded_file:
    if opcao == "Compactar":
        # To convert to a string based IO:
        stringio = str(uploaded_file.getvalue().decode("utf-8"))

        file = huffman_code.compress(uploaded_file.name)

        # Botao para baixar o .txt compactado
        btn = st.download_button(
                label="Download Arquivo Compactado",
                data=file,
                file_name="compacted_file.sl28"
            )
    else:
        pass
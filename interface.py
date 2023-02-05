import streamlit as st
import script

#Title
st.title('Trabalho final - Dupla 28')
st.write('Huffman Encoding')

uploaded_file = st.file_uploader("Escolha  seu arquivo .txt", type=["txt"])
if uploaded_file is not None:
    # To convert to a string based IO:
    stringio = str(uploaded_file.getvalue().decode("utf-8"))

    # Cria um arquivo nesse diretorio com conteúdo do arquivo original
    with open(uploaded_file.name, 'w') as f:
        f.write(stringio)

    script.compress(uploaded_file.name)
    name = uploaded_file.name.rsplit(".", 1)
    name[-1] = "sl28"
    new_filename = ".".join(name)
    script.decompress(new_filename)
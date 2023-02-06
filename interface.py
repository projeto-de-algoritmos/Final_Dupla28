import streamlit as st
import huffman_code

#Title
st.title('Trabalho final - Dupla 28')
st.write('Huffman Encoding')

st.subheader("O que deseja fazer?")
opcao = st.radio("", ("Codificar", "Descodificar"))

st.subheader("Selecione um arquivo")
uploaded_file = st.file_uploader("Escolha  seu arquivo .txt", type=["txt", "sl28"])

if uploaded_file:
    if opcao == "Codificar":
        # To convert to a string based IO:
        stringio = str(uploaded_file.getvalue().decode("utf-8"))

        # Cria um arquivo nesse diretorio com conteúdo do arquivo original
        with open(uploaded_file.name, 'w') as f:
            f.write(stringio)

        file = huffman_code.compress(uploaded_file.name)

        # Botao para baixar o .sl28
        btn = st.download_button(
                label="Download Arquivo Codificado",
                data=file,
                file_name="encoded_file.sl28"
            )
    else:

        stringio = str(uploaded_file.getvalue().decode("utf-8"))

        splitString = stringio.split("\n")

        encodedString = splitString[0]

        encodingDict = splitString[2:]

        newDict = {}
        for element in encodingDict:
            print(element.split(" "))
            if len(element.split(" "))  > 1 and len(element.split(" ")) < 3:
                newDict[element.split(" ")[0]] = element.split(" ")[1]
            elif len(element.split(" ")) == 3:
                newDict[" "] = element.split(" ")[2]

        decodedString = huffman_code.huffman_decode(encodedString, newDict)
        print(decodedString)

        # Botao para baixar o .txt descompactado
        btn = st.download_button(
                label="Download Arquivo Decodificado",
                data=decodedString,
                file_name="descodified_file.txt"
            )
## Dependências

- [deepface](https://github.com/serengil/deepface): Uma biblioteca de análise facial baseada em aprendizado profundo que oferece modelos pré-treinados para detecção de emoções faciais. Ela utiliza o TensorFlow para operações subjacentes de aprendizado profundo.
- [OpenCV](https://opencv.org/): Uma biblioteca de visão computacional de código aberto usada para processamento de imagens e vídeos.

## Uso

### Passos iniciais:

- Clone este repositório executando: `git clone https://github.com/manish-9245/Facial-Emotion-Recognition-using-OpenCV-and-Deepface.git`
- Navegue para o diretório do projeto: `cd Facial-Emotion-Recognition-using-OpenCV-and-Deepface`

1. Instale as dependências necessárias:

   - Use o comando: `pip install -r requirements.txt`
   - Ou instale as dependências individualmente:
     - `pip install deepface`
     - `pip install tf_keras`
     - `pip install opencv-python`
     - `pip install pyfirmata`

2. Baixe o arquivo XML do Haar cascade para detecção de rostos:

   - Acesse o [repositório do OpenCV no GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades) e baixe o arquivo `haarcascade_frontalface_default.xml`.

3. Execute o código:
   - Rode o script Python.
   - A webcam será ativada, e a detecção de emoções faciais em tempo real será iniciada.
   - Os rótulos das emoções serão exibidos nos quadros ao redor dos rostos detectados.

## Abordagem

1. Importe as bibliotecas necessárias: `cv2` para captura de vídeo e processamento de imagem, e `deepface` para o modelo de detecção de emoções.

2. Carregue o classificador Haar cascade usando `cv2.CascadeClassifier()`.

3. Inicie a captura de vídeo da webcam padrão com `cv2.VideoCapture()`.

4. Entre em um loop contínuo para processar cada quadro do vídeo capturado.

5. Converta cada quadro para escala de cinza usando `cv2.cvtColor()`.

6. Detecte os rostos no quadro em escala de cinza usando `face_cascade.detectMultiScale()`.

7. Para cada rosto detectado, extraia a ROI (Região de Interesse) do rosto.

8. Faça o pré-processamento da imagem do rosto para detecção de emoções usando a função de pré-processamento embutida da biblioteca `deepface`.

9. Realize as previsões das emoções utilizando o modelo pré-treinado fornecido pela biblioteca `deepface`.

10. Recupere o índice da emoção prevista e mapeie-o para o rótulo correspondente.

11. Desenhe um retângulo ao redor do rosto detectado e rotule-o com a emoção prevista usando `cv2.rectangle()` e `cv2.putText()`.

12. Exiba o quadro resultante com o rótulo da emoção usando `cv2.imshow()`.

13. Se a tecla 'q' for pressionada, saia do loop.

14. Libere a captura de vídeo e feche todas as janelas usando `cap.release()` e `cv2.destroyAllWindows()`.

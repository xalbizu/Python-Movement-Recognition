import cv2
import os

# Capturar video desde la webcam
cap = cv2.VideoCapture(0)  # El argumento 0 indica que se utilizará la primera cámara disponible
i = 0
# Leer el primer frame
ret, frame_prev = cap.read()

os.system('mkdir frames')
# Convertir el frame a escala de grises
prev_gray = cv2.cvtColor(frame_prev, cv2.COLOR_BGR2GRAY)

# Crear una ventana para mostrar el resultado
cv2.namedWindow('Detección de Movimiento', cv2.WINDOW_NORMAL)

while True:
    # Leer cada frame del video
    ret, frame = cap.read()
    
    # Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Calcular la diferencia absoluta entre los frames actual y anterior
    frame_diff = cv2.absdiff(gray, prev_gray)
    
    # Aplicar un umbral para resaltar las diferencias
    _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

    num_white = cv2.countNonZero(thresh)

    if num_white > 100:
        frame[thresh == 255] = (0, 0 , 255)
        cv2.putText(frame, 'Movimiento detectado', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imwrite('frames/'+str(i)+'_frame.jpg', frame)
        i+=1
    # Mostrar el frame resultante con las diferencias resaltadas
    cv2.imshow('Detección de Movimiento', frame)
    
    
    # Actualizar el frame anterior
    prev_gray = gray.copy()
    
    # Romper el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos y cerrar la ventana
cap.release()
cv2.destroyAllWindows()

# Crear el video a partir de los frames
video_salida = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (640, 480))
# Recorrer las imágenes y escribirlas en el video

for archivo in sorted(os.listdir('frames/'), key=lambda x: int(x.split('_')[0])):
    print(archivo)
    ruta_imagen = os.path.join('frames/', archivo)
    imagen = cv2.imread(ruta_imagen)
    video_salida.write(imagen)

# Liberar los recursos
video_salida.release()

os.system('rm -r frames/')


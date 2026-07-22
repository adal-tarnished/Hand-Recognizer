import cv2
from ultralytics import YOLO
 
def main():
    # Carga el modelo
    model = YOLO("runs/detect/train/weights/best.pt")
    
    # Inicializa la cámara con DirectShow
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # CAP_DSHOW para Windows
    
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara")
        return
    
    # Configura la resolución
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    print("Presiona 'q' para salir")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: No se pudo leer el frame")
            break
        
        # Realiza la detección
        results = model(frame, device="0")
        
        # Muestra los resultados
        annotated_frame = results[0].plot()
        cv2.imshow('Hand Detection', annotated_frame)
        
        # Salir con 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
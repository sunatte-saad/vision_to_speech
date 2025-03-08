import moondream as md
from PIL import Image
import gradio as gr
import cv2

from text_to_speech import text_to_speech
from config import MODEL_PATH, FRAME_INTERVAL, MAX_FRAMES, RESIZE_DIM, PROMPT


def initialize_model(model_path):
    print("Loading model...")
    model = md.vl(model=model_path)
    print("Model loaded successfully.")
    return model

def extract_frames(video_path, interval=FRAME_INTERVAL):
    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % interval == 0:
            print(f"Extracted frame {frame_count}")  # Debug
            frame = cv2.resize(frame, RESIZE_DIM)
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            frames.append(pil_image)
        frame_count += 1

    cap.release()
    print(f"Total frames extracted: {len(frames)}")
    return frames

def process_image_and_answer(model, image):
    encoded_image = model.encode_image(image)
    print("Image encoded successfully")
    answer = model.query(encoded_image, PROMPT)["answer"]
    print(f"Generated answer: {answer}")
    return encoded_image, answer

model = initialize_model(MODEL_PATH)

def handle_video_upload(video, history):
    if video is None:
        return "Please upload a video first.", history, None, None

    frames = extract_frames(video, interval=FRAME_INTERVAL)
    if not frames:
        return "Failed to extract frames from the video.", history, None, None

    encoded_images = []
    last_audio = None
    for i, frame in enumerate(frames[:MAX_FRAMES]):
        encoded_image, answer = process_image_and_answer(model, frame)
        encoded_images.append(encoded_image)

        audio_file = text_to_speech(answer)
        last_audio = audio_file

        history.append({"role": "user", "content": f"📹 Frame {i+1}"})
        history.append({"role": "assistant", "content": ""})  
    return "", history, encoded_images, last_audio

def handle_question(question, history, encoded_images):
    if not encoded_images:
        return "Please upload a video first.", history, None

    if question:
        answer = model.query(encoded_images[-1], question)["answer"]
        audio_file = text_to_speech(answer)  
        history.append({"role": "user", "content": ""}) 
        history.append({"role": "assistant", "content": ""})
        return "", history, encoded_images, audio_file

    return "", history, encoded_images, None

with gr.Blocks() as demo:
    gr.Markdown("# 🎥 Video to Audio Assistant (Answers Only)")
    with gr.Column():
        video_input = gr.Video(label="Upload a video")
        chat_box = gr.Chatbot(label="Chat with the Video", type='messages')
        audio_output = gr.Audio(label="Audio Response", autoplay=True)  
        question_input = gr.Textbox(label="Your Question", placeholder="Ask something about the video...")
        submit_btn = gr.Button("Ask")

    encoded_images_state = gr.State([])
    chat_history = gr.State([])

    video_input.upload(
        handle_video_upload,
        inputs=[video_input, chat_history],
        outputs=[question_input, chat_box, encoded_images_state, audio_output]  
    )

    submit_btn.click(
        handle_question,
        inputs=[question_input, chat_history, encoded_images_state],
        outputs=[question_input, chat_box, encoded_images_state, audio_output] 
    )

demo.launch(debug=True)

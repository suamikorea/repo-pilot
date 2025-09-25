import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import speech_recognition as sr
from openai import OpenAI
import os
from moviepy.editor import AudioFileClip

# API 키 불러오기
def load_api_key():
    try:
        with open("오픈AI 토큰 코드.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        messagebox.showerror("API 키 오류", "오픈AI 토큰 코드.txt 파일이 없습니다.")
        return None

def generate_response(prompt):
    api_key = load_api_key()
    if not api_key:
        return "API 키가 설정되지 않았습니다."
    
    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"GPT 응답 생성 오류: {e}"

class AudioGPTApp:
    def __init__(self, master):
        self.master = master
        master.title("SNS GPT AI 통합 프로그램")

        self.label = tk.Label(master, text="오디오 파일 선택:")
        self.label.pack()

        self.select_button = tk.Button(master, text="파일 선택", command=self.select_file)
        self.select_button.pack()

        self.start_label = tk.Label(master, text="시작 시간 (초):")
        self.start_label.pack()
        self.start_entry = tk.Entry(master)
        self.start_entry.pack()

        self.end_label = tk.Label(master, text="끝 시간 (초):")
        self.end_label.pack()
        self.end_entry = tk.Entry(master)
        self.end_entry.pack()

        self.play_button = tk.Button(master, text="재생", command=self.play_audio)
        self.play_button.pack()

        self.recognize_button = tk.Button(master, text="음성 인식 및 GPT 응답", command=self.recognize_and_respond)
        self.recognize_button.pack()

        self.response_text = tk.Text(master, height=12, width=60)
        self.response_text.pack()

        self.audio_path = None

    def select_file(self):
        self.audio_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if self.audio_path:
            messagebox.showinfo("파일 선택됨", f"선택된 파일: {self.audio_path}")

    def play_audio(self):
        if not self.audio_path:
            messagebox.showerror("오류", "먼저 오디오 파일을 선택하세요.")
            return

        try:
            start_sec = int(self.start_entry.get())
            end_sec = int(self.end_entry.get())
        except ValueError:
            messagebox.showerror("입력 오류", "시작/끝 시간을 숫자로 입력하세요.")
            return

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.audio_path)
        pygame.mixer.music.play(start=start_sec)

        self.master.after((end_sec - start_sec) * 1000, self.stop_audio)

    def stop_audio(self):
        pygame.mixer.music.stop()
        pygame.quit()

    def recognize_and_respond(self):
        if not self.audio_path:
            messagebox.showerror("오류", "먼저 오디오 파일을 선택하세요.")
            return

        recognizer = sr.Recognizer()
        audio_clip = AudioFileClip(self.audio_path)
        audio_clip.write_audiofile("temp.wav")

        with sr.AudioFile("temp.wav") as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language='ko-KR')
        except sr.UnknownValueError:
            text = "음성을 이해하지 못했습니다."
        except sr.RequestError as e:
            text = f"Google 음성 인식 서비스 오류: {e}"

        response = generate_response(text)
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, f"🎙️ 인식된 텍스트:\n{text}\n\n🤖 GPT 응답:\n{response}")

        with open("GPT_응답_결과.txt", "w", encoding="utf-8") as f:
            f.write(f"인식된 텍스트:\n{text}\n\nGPT 응답:\n{response}")

        os.remove("temp.wav")

# GUI 실행
root = tk.Tk()
app = AudioGPTApp(root)
root.mainloop()
# Audio GPT App - SNS GPT AI 통합 프로그램

오디오 파일을 처리하여 음성 인식과 GPT 응답을 생성하는 프로그램입니다.

## 주요 기능

### 🎵 오디오 처리
- MP3, WAV 오디오 파일 선택 및 로드
- 특정 시간 구간 오디오 재생 (시작/끝 시간 지정)
- 오디오 파일을 WAV 형식으로 변환하여 음성 인식

### 🎙️ 음성 인식
- Google Speech Recognition API를 사용한 한국어 음성 인식
- 오디오 파일의 음성 내용을 텍스트로 변환
- 인식 실패 시 오류 메시지 표시

### 🤖 GPT 통합
- OpenAI GPT-4 모델을 사용한 자동 응답 생성
- 인식된 텍스트를 바탕으로 지능적인 응답 생성
- API 키 파일을 통한 안전한 인증 관리

### 💾 결과 저장
- 인식된 텍스트와 GPT 응답을 파일로 저장
- UTF-8 인코딩으로 한글 완벽 지원
- 결과 파일: `GPT_응답_결과.txt`

## 설치 방법

1. **Python 3.8 이상 설치** (필수)

2. **필요한 패키지 설치**:
```bash
pip install -r requirements.txt
```

3. **OpenAI API 키 설정**:
   - [OpenAI 플랫폼](https://platform.openai.com/api-keys)에서 API 키 발급
   - `오픈AI 토큰 코드.txt.template` 파일을 참고하여 `오픈AI 토큰 코드.txt` 파일 생성
   - 발급받은 API 키를 파일에 저장

## 사용 방법

### 1. 프로그램 실행
```bash
python audio_gpt_app.py
```

또는 런처 사용:
```bash
python launch_audio_gpt.py
```

### 2. 오디오 파일 선택
- "파일 선택" 버튼 클릭
- MP3 또는 WAV 파일 선택

### 3. 재생 구간 설정 (선택사항)
- 시작 시간(초) 입력
- 끝 시간(초) 입력
- "재생" 버튼으로 해당 구간 미리 듣기

### 4. 음성 인식 및 GPT 응답
- "음성 인식 및 GPT 응답" 버튼 클릭
- 자동으로 음성 인식 후 GPT 응답 생성
- 결과가 텍스트 박스에 표시됨

## 파일 구조

```
audio_gpt_app.py              # 메인 프로그램
launch_audio_gpt.py           # 런처 스크립트
test_audio_gpt_app.py         # 테스트 스크립트
오픈AI 토큰 코드.txt.template  # API 키 템플릿
requirements.txt              # 필요한 패키지 목록
README_AUDIO_GPT.md          # 이 문서
```

## 의존성 패키지

- `tkinter`: GUI 인터페이스 (Python 기본 포함)
- `pygame`: 오디오 재생
- `SpeechRecognition`: 음성 인식
- `openai`: OpenAI API 연동
- `moviepy`: 오디오/비디오 처리
- `Pillow`: 이미지 처리 지원

## 시스템 요구사항

- **운영체제**: Windows, macOS, Linux
- **Python**: 3.8 이상
- **메모리**: 최소 512MB RAM
- **네트워크**: 인터넷 연결 (음성 인식 및 GPT API 사용)
- **오디오**: 스피커 또는 헤드폰 (오디오 재생용)

## 사용 예시

1. **오디오 파일 처리**:
   - 팟캐스트나 강의 오디오에서 특정 구간의 내용을 텍스트로 변환
   - 음성 메모를 텍스트로 변환하여 문서화

2. **GPT 기반 요약**:
   - 긴 오디오 내용을 GPT로 요약
   - 오디오 내용에 대한 질문과 답변 생성

3. **언어 학습**:
   - 외국어 오디오의 발음과 내용 확인
   - GPT를 통한 언어 교정 및 설명

## 문제 해결

### 자주 발생하는 오류

1. **"tkinter 모듈을 찾을 수 없습니다"**
   - Windows: Python 재설치 시 "tcl/tk and IDLE" 옵션 체크
   - Linux: `sudo apt-get install python3-tk`
   - macOS: Python.org에서 공식 Python 설치

2. **"pygame 초기화 오류"**
   - 오디오 드라이버 확인
   - 다른 프로그램에서 오디오 장치 사용 중인지 확인

3. **"Google 음성 인식 서비스 오류"**
   - 인터넷 연결 확인
   - 잠시 후 다시 시도 (API 한도 초과 가능성)

4. **"OpenAI API 오류"**
   - API 키 유효성 확인
   - OpenAI 계정 잔액 확인
   - API 키 파일 경로 및 형식 확인

### 로그 및 디버깅

- 프로그램 실행 중 발생하는 오류는 콘솔에 출력됩니다
- 임시 파일 `temp.wav`가 생성되었다가 자동 삭제됩니다
- 결과 파일 `GPT_응답_결과.txt`에서 마지막 처리 결과 확인 가능

## 보안 주의사항

- `오픈AI 토큰 코드.txt` 파일을 공유하지 마세요
- API 키는 개인적으로 관리하고 정기적으로 교체하세요
- 프로그램 종료 시 임시 파일들이 자동으로 삭제되는지 확인하세요

## 라이선스

이 프로젝트는 개인 실험용 프로그램입니다.
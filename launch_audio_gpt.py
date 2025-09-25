#!/usr/bin/env python3
"""
Audio GPT App 런처 스크립트
의존성 확인 후 오디오 GPT 프로그램을 실행합니다.
"""

import sys
import subprocess
import os

def check_audio_dependencies():
    """오디오 GPT 앱에 필요한 의존성 확인"""
    required_modules = [
        ('tkinter', 'tkinter (usually pre-installed)'),
        ('pygame', 'pygame'),
        ('speech_recognition', 'SpeechRecognition'),
        ('openai', 'openai'),
        ('moviepy', 'moviepy'),
        ('PIL', 'Pillow')
    ]
    
    missing_modules = []
    available_modules = []
    
    for module, package in required_modules:
        try:
            __import__(module)
            available_modules.append(package)
        except ImportError:
            missing_modules.append(package)
    
    return available_modules, missing_modules

def check_api_key():
    """API 키 파일 존재 확인"""
    api_key_file = "오픈AI 토큰 코드.txt"
    template_file = "오픈AI 토큰 코드.txt.template"
    
    if os.path.exists(api_key_file):
        return True, "API 키 파일이 있습니다."
    elif os.path.exists(template_file):
        return False, f"API 키 파일이 없습니다. {template_file}을 참고하여 {api_key_file}을 만들어주세요."
    else:
        return False, f"API 키 파일과 템플릿이 모두 없습니다. {api_key_file}을 만들어주세요."

def install_dependencies():
    """누락된 의존성 설치"""
    print("필요한 패키지를 설치하고 있습니다...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("=== Audio GPT App 런처 ===")
    print("SNS GPT AI 통합 프로그램 (오디오 버전)")
    
    # 의존성 확인
    available, missing = check_audio_dependencies()
    
    print(f"\n사용 가능한 모듈: {len(available)}개")
    print(f"누락된 모듈: {len(missing)}개")
    
    if missing:
        print(f"\n누락된 패키지:")
        for package in missing:
            print(f"  - {package}")
        
        response = input("\n자동으로 설치하시겠습니까? (y/n): ").lower()
        
        if response == 'y':
            if install_dependencies():
                print("✓ 패키지 설치 완료!")
                # 재확인
                available, missing = check_audio_dependencies()
            else:
                print("✗ 패키지 설치 실패!")
                print("수동으로 설치해주세요: pip install -r requirements.txt")
                return
        else:
            print("의존성을 먼저 설치해주세요: pip install -r requirements.txt")
            return
    
    # API 키 확인
    api_key_ok, api_message = check_api_key()
    print(f"\nAPI 키 상태: {api_message}")
    
    if not api_key_ok:
        print("주의: API 키가 없으면 GPT 응답 기능을 사용할 수 없습니다.")
        response = input("계속 진행하시겠습니까? (y/n): ").lower()
        if response != 'y':
            return
    
    # 프로그램 실행
    if not missing:
        print("\n✓ 모든 의존성이 준비되었습니다!")
        
        try:
            print("Audio GPT 프로그램을 시작합니다...")
            print("(GUI 창이 열리지 않으면 Xvfb나 GUI 환경을 확인해주세요)")
            
            # 메인 프로그램 실행
            import audio_gpt_app
            
        except ImportError as e:
            print(f"✗ 모듈 로딩 오류: {e}")
            print("테스트 모드로 실행합니다...")
            subprocess.run([sys.executable, 'test_audio_gpt_app.py'])
        except Exception as e:
            print(f"✗ GUI 실행 오류: {e}")
            print("GUI 환경이 없거나 오류가 발생했습니다.")
            print("테스트 모드로 실행합니다...")
            subprocess.run([sys.executable, 'test_audio_gpt_app.py'])
    else:
        print("의존성 설치가 필요합니다.")

if __name__ == "__main__":
    main()
# 'Hello Mars' 출력
print("Hello Mars")

# mission_computer_main.log 파일 로그 출력 (예외처리 포함)
log_file_path = 'mission_computer_main.log'
try:
    with open(log_file_path, 'r', encoding='utf-8') as log_file:
        for line in log_file:
            print(line.strip())  # 앞/뒤 공백 제거
except FileNotFoundError:
    print(f"[에러] 파일을 찾을 수 없습니다: {log_file_path}")
except PermissionError:
    print(f"[에러] 파일에 접근할 권한이 없습니다: {log_file_path}")
except UnicodeDecodeError:
    print(f"[에러] 파일 인코딩 오류입니다. 인코딩을 확인해주세요: {log_file_path}")
except Exception as e:
    print(f"[에러] 예기치 못한 오류가 발생했습니다: {e}")


# 보고서 작성
# -> log_analysis.md 파일 참고
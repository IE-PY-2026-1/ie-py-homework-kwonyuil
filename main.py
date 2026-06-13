# 파일이름 :baseball
# 작 성 자 :kwonyuil
players = []


# 파일 불러오기
def load_file():
    global players

    try:
        with open("player_data.txt", "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(",")

                name = data[0]
                avg = float(data[1])
                steal = int(data[2])
                field = float(data[3])
                arm = float(data[4])
                slg = float(data[5])

                players.append([name, avg, steal, field, arm, slg])

        print("저장된 데이터를 불러왔습니다.")

    except FileNotFoundError:
        print("저장된 파일이 없습니다. 새로 시작합니다.")


# 파일 저장
def save_file():
    try:
        with open("player_data.txt", "w", encoding="utf-8") as file:

            for player in players:
                line = ""

                for i in range(len(player)):
                    line += str(player[i])

                    if i != len(player) - 1:
                        line += ","

                file.write(line + "\n")

        print("파일 저장 완료!")

    except Exception:
        print("파일 저장 중 오류 발생")


def input_players():
    global players

    try:
        n = int(input("선수 몇 명 입력할까요? "))

        for i in range(n):
            print(f"\n{i+1}번째 선수 입력")

            name = input("이름: ")

            try:
                avg = float(input("타율: "))
                steal = int(input("도루 개수: "))
                field = float(input("수비율: "))
                arm = float(input("송구 속도(mph): "))
                slg = float(input("장타율: "))

            except ValueError:
                print("숫자를 올바르게 입력하세요.")
                continue

            player = [name, avg, steal, field, arm, slg]

            # append 사용 (과제 필수)
            players.append(player)

    except ValueError:
        print("인원 수는 숫자로 입력하세요.")


def analyze(players):
    print("\n===== 결과 =====")

    count_5tool = 0

    print(f"총 선수 수: {len(players)}")

    if len(players) == 0:
        print("등록된 선수가 없습니다.")
        return 0

    avg_list = []

    for p in players:
        avg_list.append(p[1])

    max_avg = max(avg_list)

    for i in range(len(players)):
        p = players[i]

        name = p[0]
        avg = p[1]
        steal = p[2]
        field = p[3]
        arm = p[4]
        slg = p[5]

        if avg >= 0.280 and steal >= 20 and field >= 0.980 and arm >= 85 and slg >= 0.450:
            result = "5툴 플레이어"
            count_5tool += 1

        else:
            if slg >= 0.450 and steal >= 20:
                result = "호타준족"
            elif field >= 0.995:
                result = "수비 장인"
            else:
                result = "일반 선수"

        print(f"\n{i+1}번째 선수")
        print(f"이름: {name}")
        print(f"판정: {result}")

    for p in players:
        if p[1] == max_avg:
            print(f"\n타격왕: {p[0]} (타율: {p[1]})")

    print(f"\n5툴 플레이어 수: {count_5tool}")

    return count_5tool


# 이중리스트 출력
def show_players():

    print("\n===== 전체 선수 데이터 =====")

    if len(players) == 0:
        print("등록된 선수가 없습니다.")
        return

    print("이름\t타율\t도루\t수비율\t송구속도\t장타율")

    # 이중 순회
    for player in players:
        for item in player:
            print(item, end="\t")
        print()


load_file()

while True:

    print("\n===== KBO 타자 5툴 플레이어 판정 시스템 =====")
    print("1. 선수 입력")
    print("2. 선수 조회")
    print("3. 선수 분석")
    print("4. 파일 저장")
    print("5. 종료")

    choice = input("메뉴 선택: ")

    if choice == "1":
        input_players()

    elif choice == "2":
        show_players()

    elif choice == "3":
        analyze(players)

    elif choice == "4":
        save_file()

    elif choice == "5":
        save_file()
        print("프로그램 종료")
        break

    else:
        print("잘못된 입력입니다.")

# 파일이름 :baseball
# 작 성 자 :kwonyuil
players = []


def input_players():
    global players

    n = int(input("선수 몇 명 입력할까요? "))

    for i in range(n):
        print(f"\n{i+1}번째 선수 입력")

        name = input("이름: ")
        avg = float(input("타율: "))
        steal = int(input("도루 개수: "))
        field = float(input("수비율: "))
        arm = float(input("송구 속도(mph): "))
        slg = float(input("장타율: "))

        player = [name, avg, steal, field, arm, slg]
        players.insert(len(players), player)


def analyze(players):   # 매개변수 사용
    print("\n===== 결과 =====")

    count_5tool = 0

    print(f"총 선수 수: {len(players)}")

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

    return count_5tool   # return 사용


def show_players():
    print("\n===== 선수 목록 =====")
    for p in players:
        print(p[0])


while True:
    print("\n===== KBO 타자 5툴 플레이어 판정 시스템 =====")
    print("1. 선수 입력")
    print("2. 선수 조회")
    print("3. 분석")
    print("4. 종료")

    choice = input("메뉴 선택: ")

    if choice == "1":
        input_players()

    elif choice == "2":
        show_players()

    elif choice == "3":
        analyze(players)

    elif choice == "4":
        print("프로그램 종료")
        break

    else:
        print("잘못된 입력입니다.")

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "코로나 종식 게임.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J5A9p2-QvGRc",
        "outputId": "5ec8efb9-e940-457a-8899-e180d82c1783"
      },
      "source": [
        "import random\r\n",
        "from operator import itemgetter\r\n",
        "\r\n",
        "class CovidGame:\r\n",
        "    isOver = False\r\n",
        "    round = 1\r\n",
        "    increasedInfection = 0\r\n",
        "    curedPatient = 0\r\n",
        "    curedCountry = []\r\n",
        "\r\n",
        "    def __init__(self, vac_list, cou_list):\r\n",
        "        self.vac_list = vac_list[:]\r\n",
        "        self.cou_list = cou_list[:]\r\n",
        "    \r\n",
        "    def roundStart(self, vac, cou):\r\n",
        "            print(\"★\", self.round , \"번째 시도 ★\\n\")\r\n",
        "            print(\"선택된 백신 :\", self.vac_list[vac][0] + \",\", \"치료율 :\", self.vac_list[vac][1] * 100, \"%\")\r\n",
        "            print(\"선택된 나라 :\", self.cou_list[cou][0]+ \",\" , \"인구수 :\", str(self.cou_list[cou][1])+ \",\", \"감염자수 :\", self.cou_list[cou][2])\r\n",
        "            self.curedPatient += int(self.cou_list[cou][2] * (1 - self.vac_list[vac][1]))\r\n",
        "            self.cou_list[cou][2] = int(self.cou_list[cou][2] * (1 - self.vac_list[vac][1]))\r\n",
        "\r\n",
        "            print(\"=================================================\")\r\n",
        "            if self.cou_list[cou][2] == 0:\r\n",
        "                print(\"완치 된 국가:\", self.cou_list[cou][0])\r\n",
        "                self.curedCountry.append(self.cou_list.pop(cou))         \r\n",
        "\r\n",
        "\r\n",
        "    def isGameOver(self):\r\n",
        "        for i in range(len(self.cou_list)):\r\n",
        "            if self.cou_list[i][2] >= self.cou_list[i][1]:\r\n",
        "                self.isOver = True\r\n",
        "        if self.round >= 6:\r\n",
        "            self.isOver = True\r\n",
        "    \r\n",
        "    def roundEnd(self):\r\n",
        "        for i in range(len(self.cou_list)):\r\n",
        "            self.cou_list[i][2] += int(self.cou_list[i][1] * 0.15)\r\n",
        "            self.increasedInfection += int(self.cou_list[i][1] * 0.15)\r\n",
        "        if len(self.cou_list) == 0:\r\n",
        "            print(\"모든 국가가 완치되었습니다 !!!\")\r\n",
        "        random.shuffle(self.vac_list)\r\n",
        "        random.shuffle(self.cou_list)\r\n",
        "        self.round += 1\r\n",
        "\r\n",
        "    def printResult(self):\r\n",
        "        print(str(self.round) + \"차 백신 투여 후 감염된 나라에 대한 정보\")\r\n",
        "        print(\"=================================================\")\r\n",
        "        for country in self.cou_list:\r\n",
        "            print(\"감염 국가 :\", country[0])\r\n",
        "            print(\"인구수 :\", country[1])\r\n",
        "            print(\"감염 인구수 :\", country[2])\r\n",
        "            print(\"\")\r\n",
        "    \r\n",
        "    def GameOver(self):\r\n",
        "        print(\"=================================================\")\r\n",
        "        print(\"                     최종결과                    \")\r\n",
        "        print(\"=================================================\")\r\n",
        "        print(\"라운드마다 추가로 감염된 감염자 수:\", str(self.increasedInfection)+\"명\")\r\n",
        "        print(\"백신으로 치료된 감염자 수:\", str(self.curedPatient)+\"명\")\r\n",
        "        print(\"백신으로 완치된 국가:\", end = \" \")\r\n",
        "        for cured in self.curedCountry:\r\n",
        "            print(cured[0], end = \" \")\r\n",
        "        print(\"(\", len(self.curedCountry), \"개)\")\r\n",
        "\r\n",
        "        country = self.curedCountry[:] + self.cou_list[:]\r\n",
        "        country = sorted(country , key = itemgetter(2))\r\n",
        "\r\n",
        "        for i in range(5):\r\n",
        "            print(str(i + 1) + \"위\")\r\n",
        "            print(\"감염 국가 :\", country[4 - i][0])\r\n",
        "            print(\"인구수 :\", country[4 - i][1])\r\n",
        "            print(\"감염 인구수 :\", country[4 - i][2])\r\n",
        "            print(\"\")\r\n",
        "        print(\"게임 종료!\")\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "termination = False\r\n",
        "\r\n",
        "choose = 0\r\n",
        "\r\n",
        "vac_list = [[\"백신1\", 0.25], [\"백신2\", 0.5], [\"백신3\", 1]]\r\n",
        "cou_list = [[\"한국\", 1500, 300], [\"중국\", 3000, 800],[\"일본\", 2000, 500], [\"미국\", 2500, 750],[\"독일\", 2200, 1000]]\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "while not termination:\r\n",
        "    print(\"--------------------------\")\r\n",
        "    print(\"     코로나 종식 게임     \")\r\n",
        "    print(\"--------------------------\")\r\n",
        "    print(\"1. 백신 정보\")\r\n",
        "    print(\"2. 감염된 국가 정보\")\r\n",
        "    print(\"3. 게임 시작\")\r\n",
        "    print(\"4. 게임 종료\")\r\n",
        "    try:\r\n",
        "        choose = int(input())\r\n",
        "    except ValueError:\r\n",
        "        print(\"오류가 발생했습니다. 숫자를 입력해주세요.\")\r\n",
        "        choose = 0\r\n",
        "\r\n",
        "    if choose == 1:\r\n",
        "        for vaccine in vac_list:\r\n",
        "            print(\"백신 이름 : \" + vaccine[0])\r\n",
        "            print(\"백신 치료율 : \"+ str(vaccine[1]*100) + \"%\")\r\n",
        "            print(\"\")\r\n",
        "\r\n",
        "    elif choose == 2:\r\n",
        "        for country in cou_list:\r\n",
        "            print(\"감염 국가 :\", country[0])\r\n",
        "            print(\"인구수 :\", country[1])\r\n",
        "            print(\"감염 인구수 :\", country[2])\r\n",
        "            print(\"\")\r\n",
        "\r\n",
        "    elif choose == 3:\r\n",
        "        game = CovidGame(vac_list, cou_list)\r\n",
        "        print(\"사용할 백신(1~3)과 백신을 적용할 국가(1~5)의 번호를 차례대로 입력하세요\")\r\n",
        "        while True:\r\n",
        "            try:\r\n",
        "                vac, cou = input().split()\r\n",
        "                vac = int(vac)\r\n",
        "                cou = int(cou)\r\n",
        "                break;\r\n",
        "            except ValueError:\r\n",
        "                print(\"오류가 발생했습니다. 숫자를 입력해주세요.\")\r\n",
        "\r\n",
        "        while not game.isOver:\r\n",
        "            if game.round == 1:\r\n",
        "                game.roundStart(vac, cou)\r\n",
        "            else :\r\n",
        "                game.roundStart(random.randint(0,2), random.randint(0,len(game.cou_list) - 1))\r\n",
        "            game.printResult()\r\n",
        "            game.roundEnd()\r\n",
        "            game.isGameOver()\r\n",
        "       \r\n",
        "        game.GameOver()\r\n",
        "\r\n",
        "    elif choose == 4:\r\n",
        "        termination = True\r\n"
      ],
      "execution_count": None,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "--------------------------\n",
            "     코로나 종식 게임     \n",
            "--------------------------\n",
            "1. 백신 정보\n",
            "2. 감염된 국가 정보\n",
            "3. 게임 시작\n",
            "4. 게임 종료\n",
            "3\n",
            "사용할 백신(1~3)과 백신을 적용할 국가(1~5)의 번호를 차례대로 입력하세요\n",
            "1 1\n",
            "★ 1 번째 시도 ★\n",
            "\n",
            "선택된 백신 : 백신2, 치료율 : 50.0 %\n",
            "선택된 나라 : 중국, 인구수 : 3000, 감염자수 : 800\n",
            "=================================================\n",
            "1차 백신 투여 후 감염된 나라에 대한 정보\n",
            "=================================================\n",
            "감염 국가 : 한국\n",
            "인구수 : 1500\n",
            "감염 인구수 : 300\n",
            "\n",
            "감염 국가 : 중국\n",
            "인구수 : 3000\n",
            "감염 인구수 : 400\n",
            "\n",
            "감염 국가 : 일본\n",
            "인구수 : 2000\n",
            "감염 인구수 : 500\n",
            "\n",
            "감염 국가 : 미국\n",
            "인구수 : 2500\n",
            "감염 인구수 : 750\n",
            "\n",
            "감염 국가 : 독일\n",
            "인구수 : 2200\n",
            "감염 인구수 : 1000\n",
            "\n",
            "★ 2 번째 시도 ★\n",
            "\n",
            "선택된 백신 : 백신1, 치료율 : 25.0 %\n",
            "선택된 나라 : 한국, 인구수 : 1500, 감염자수 : 525\n",
            "=================================================\n",
            "2차 백신 투여 후 감염된 나라에 대한 정보\n",
            "=================================================\n",
            "감염 국가 : 미국\n",
            "인구수 : 2500\n",
            "감염 인구수 : 1125\n",
            "\n",
            "감염 국가 : 일본\n",
            "인구수 : 2000\n",
            "감염 인구수 : 800\n",
            "\n",
            "감염 국가 : 중국\n",
            "인구수 : 3000\n",
            "감염 인구수 : 850\n",
            "\n",
            "감염 국가 : 독일\n",
            "인구수 : 2200\n",
            "감염 인구수 : 1330\n",
            "\n",
            "감염 국가 : 한국\n",
            "인구수 : 1500\n",
            "감염 인구수 : 393\n",
            "\n",
            "★ 3 번째 시도 ★\n",
            "\n",
            "선택된 백신 : 백신2, 치료율 : 50.0 %\n",
            "선택된 나라 : 중국, 인구수 : 3000, 감염자수 : 1300\n",
            "=================================================\n",
            "3차 백신 투여 후 감염된 나라에 대한 정보\n",
            "=================================================\n",
            "감염 국가 : 일본\n",
            "인구수 : 2000\n",
            "감염 인구수 : 1100\n",
            "\n",
            "감염 국가 : 독일\n",
            "인구수 : 2200\n",
            "감염 인구수 : 1660\n",
            "\n",
            "감염 국가 : 미국\n",
            "인구수 : 2500\n",
            "감염 인구수 : 1500\n",
            "\n",
            "감염 국가 : 한국\n",
            "인구수 : 1500\n",
            "감염 인구수 : 618\n",
            "\n",
            "감염 국가 : 중국\n",
            "인구수 : 3000\n",
            "감염 인구수 : 650\n",
            "\n",
            "★ 4 번째 시도 ★\n",
            "\n",
            "선택된 백신 : 백신3, 치료율 : 100 %\n",
            "선택된 나라 : 일본, 인구수 : 2000, 감염자수 : 1400\n",
            "=================================================\n",
            "완치 된 국가: 일본\n",
            "4차 백신 투여 후 감염된 나라에 대한 정보\n",
            "=================================================\n",
            "감염 국가 : 독일\n",
            "인구수 : 2200\n",
            "감염 인구수 : 1990\n",
            "\n",
            "감염 국가 : 중국\n",
            "인구수 : 3000\n",
            "감염 인구수 : 1100\n",
            "\n",
            "감염 국가 : 한국\n",
            "인구수 : 1500\n",
            "감염 인구수 : 843\n",
            "\n",
            "감염 국가 : 미국\n",
            "인구수 : 2500\n",
            "감염 인구수 : 1875\n",
            "\n",
            "=================================================\n",
            "                     최종결과                    \n",
            "=================================================\n",
            "라운드마다 추가로 감염된 감염자 수: 6420명\n",
            "백신으로 치료된 감염자 수: 1443명\n",
            "백신으로 완치된 국가: 일본 ( 1 개)\n",
            "1위\n",
            "감염 국가 : 독일\n",
            "인구수 : 2200\n",
            "감염 인구수 : 2320\n",
            "\n",
            "2위\n",
            "감염 국가 : 미국\n",
            "인구수 : 2500\n",
            "감염 인구수 : 2250\n",
            "\n",
            "3위\n",
            "감염 국가 : 중국\n",
            "인구수 : 3000\n",
            "감염 인구수 : 1550\n",
            "\n",
            "4위\n",
            "감염 국가 : 한국\n",
            "인구수 : 1500\n",
            "감염 인구수 : 1068\n",
            "\n",
            "5위\n",
            "감염 국가 : 일본\n",
            "인구수 : 2000\n",
            "감염 인구수 : 0\n",
            "\n",
            "게임 종료!\n",
            "--------------------------\n",
            "     코로나 종식 게임     \n",
            "--------------------------\n",
            "1. 백신 정보\n",
            "2. 감염된 국가 정보\n",
            "3. 게임 시작\n",
            "4. 게임 종료\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
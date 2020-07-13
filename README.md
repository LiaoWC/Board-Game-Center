# README

### 如何運行網頁？
1. Change your work directory to venv.
    ```shell
    cd venv
    ```
2. Activate the python virtual environment.
    ```shell
    source bin/activate
    ```
3. Use python3 to run the main.py.
    ```shell
    sudo python3 main.py
    ```
4. Open your web-browser(Chrome is recommended.) and go to `0.0.0.0`
### 備註：
- 本程式於Ubuntu18.04上撰寫，若其它作業系統在運行上有問題可以試試使用Ubuntu18.04。
- 可以通過修改main.py的`ifDebegMode`(True or False)，來開關Flask的debug模式。
- 目前設成網頁會跑在localhost的port 80，所以需要sudo的權限。可以在main.py的`app.run`那邊修改運行的網址與port。

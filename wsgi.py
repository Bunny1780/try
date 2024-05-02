def application(environ, start_response):
    # 定義 HTTP 回應狀態和標頭
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    
    # 取得 HTTP 請求中的 PATH_INFO
    path = environ.get('PATH_INFO', '/')
    
    # 根據不同的路徑返回不同的內容
    if path == '/':
        response_body = b'Hello, World!'
    elif path == '/about':
        response_body = b'About Page'
    else:
        response_body = b'Page Not Found'
        status = '404 Not Found'
    
    # 呼叫 start_response 函式來設置回應的狀態和標頭
    start_response(status, headers)
    
    # 返回回應內容
    return [response_body]

# 如果這個檔案被當作模組引入，則不會執行以下程式碼
if __name__ == '__main__':
    # 使用內建的 WSGI HTTP 伺服器來運行應用程式
    from wsgiref.simple_server import make_server
    
    # 建立一個 WSGI 伺服器並設定應用程式
    httpd = make_server('localhost', 8000, application)
    print("Serving HTTP on port 8000...")
    
    # 監聽連接
    httpd.serve_forever()
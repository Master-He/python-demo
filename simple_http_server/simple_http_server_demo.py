import http.server
import socketserver

PORT = 7777  # 指定监听的端口号

# 创建一个HTTP请求处理器
handler = http.server.SimpleHTTPRequestHandler

# 创建一个TCP服务器，监听指定端口
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("serving at port", PORT)
    # 开始监听请求，直到用户按下Ctrl+C
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

# 关闭服务器
httpd.server_close()

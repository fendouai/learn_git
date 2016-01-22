import urllib

WEIXIN_APPID="WEIXIN_APPID";
WEIXIN_APPSECRET="WEIXIN_APPSECRET";
WEIXIN_HOST="https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid="
TOKEN_HOST=WEIXIN_HOST+WEIXIN_APPID+"&secret="+WEIXIN_APPSECRET
print TOKEN_HOST
token = urllib.urlopen(TOKEN_HOST)
print token.read()
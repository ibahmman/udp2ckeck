# تست دسترس پذیری پورت UDP – UDP Echo 

یک سرور **UDP Echo ساده** به زبان پایتون که پیام‌های UDP را دریافت و همان پیام را به فرستنده بازمی‌گرداند.
ایده‌آل برای تست سریع ارتباط UDP یا ایجاد یک سرویس echo ساده.

---

## ویژگی‌ها

* بدون نیاز به نصب پکیج اضافی، فقط با پایتون استاندارد
* قابل تنظیم **آدرس میزبان (host)** و **پورت** از طریق خط فرمان
* قابلیت اجرا مستقیم با `curl | python3 -`
* نمایش پیام‌های دریافتی در ترمینال

---

## پیش‌نیازها

* Python 3.x
* `curl` یا `wget` (اختیاری، برای اجرای یک‌خطی)
* `netcat` (nc) یا `socat` برای تست (اختیاری)

---

## اجرای سرور

### اجرای مستقیم با یک خط

```bash
curl -sSL https://raw.githubusercontent.com/ibahmman/udp2ckeck/main/main.py | python3 - --host <HOST> --port <PORT>
```

نمونه:

```bash
curl -sSL https://raw.githubusercontent.com/ibahmman/udp2ckeck/main/main.py | python3 - --host 141.11.246.33 --port 8888
```

پاسخ:

```
UDP server listening on 141.11.246.33:8888
```

برای بستن سرور: `Ctrl+C`

---

### اجرای محلی (اختیاری)

```bash
wget https://raw.githubusercontent.com/ibahmman/udp2ckeck/main/main.py
python3 main.py --host 0.0.0.0 --port 9999
```

---

## تست سرور

### با Netcat (`nc`)

```bash
echo "Hello UDP" | nc -u <SERVER_IP> <PORT>
```

نمونه:

```bash
echo "Hello UDP" | nc -u 141.11.246.33 8888
```

> نکته: برای برخی نسخه‌های nc:

```bash
echo "Hello UDP" | nc -u -w1 141.11.246.33 8888
```

---

### با Socat

```bash
socat - UDP:141.11.246.33:8888
```

پیام تایپ کنید و Enter بزنید؛ سرور پیام را echo می‌کند.

---

## آرگومان‌های خط فرمان

| آرگومان  | پیش‌فرض   | توضیح                           |
| -------- | --------- | ------------------------------- |
| `--host` | `0.0.0.0` | آی‌پی یا میزبان برای اتصال سرور |
| `--port` | `9999`    | پورتی که سرور به آن گوش می‌دهد  |

---

## نکات

* مطمئن شوید پورت UDP در فایروال باز است
* UDP بدون اتصال (connectionless) است؛ ممکن است برخی پیام‌ها گم شوند
* توصیه می‌شود از پورت بالای 1024 استفاده کنید

---

## لایسنس

MIT License – استفاده، تغییر و انتشار آزاد است (بهمن رشنو | چلسرو)

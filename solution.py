from socket import *


def smtp_client(port = 1025, mailserver = '127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    import socket
    import sys

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #print('Client Socket Created')

    host = 'www.google.com'
    port = 80

    server_address = (mailserver, port)

    remote_ip = socket.gethostbyname(host)
    #print('IP address of' + host + 'is ' + remote_ip)

    clientSocket.connect((remote_ip, port))
    #print('Socket Connected to' + host + 'on IP' + remote_ip)
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)

    clientSocket.close()

    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    import smtplib

    sender_mail = smtplib.SMTP('tnicoledavis@gmail.com', 587)

    sender_mail.starttls()

    sender_mail.login("tnicoledavis@gmail.com", "144_Misha")

    message = "Hi, this is Tamisha and I hope you receive this in good health."

    sender_mail.sendmail("tnicoledavis@gamail.com", "td2191@nyu.edu")

    sender_mail.quit()
   # Fill in end

   # Send RCPT TO command and print server response.
   # Fill in start

   # Fill in end

   # Send DATA command and print server response.
   # Fill in start

   # Fill in end

   # Send message data.
   # Fill in start
   # Fill in end

   # Message ends with a single period.
   # Fill in start
   # Fill in end

   # Send QUIT command and get server response.
   # Fill in start
   # Fill in end


if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')

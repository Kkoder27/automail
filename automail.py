import ezgmail, re, time

while True:
    recThreads = ezgmail.recent()
    findEmail = re.compile(r'<(.*)@(.*)>')
    i = 0
    for msg in recThreads:
        subEval = recThreads[i].messages[0].subject.split(' ')
        sender = recThreads[i].messages[0].sender
        if subEval[0] == 'Nick' and subEval[1] == 'says:':
            subEval.remove('Nick')
            subEval.remove('says:')
            replyAddress = findEmail.search(sender).group(0).replace('<','').replace('>','')
            replyContent = 'I am now doing ' + ' '.join(subEval)
            ezgmail.send(replyAddress, replyContent, replyContent)
            ezgmail._trash(recThreads[i])
        i += 1
    time.sleep(60)
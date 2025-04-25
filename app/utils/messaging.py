def format_message(message):
    return {
        "id": message.id,
        "sender": message.sender_id,
        "receiver": message.receiver_id,
        "content": message.content,
        "read": message.read,
        "sent_at": message.sent_at.isoformat()
    }

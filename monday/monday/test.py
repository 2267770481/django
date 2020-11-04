def seat(bucket: list) -> int:
    """
        Check the bucket and return the max distance position
    :param bucket: this is a list. Integer number 1 means someone and 0 means nobody.
    :return:  Maximum distance position
        example:
            bucket = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
            res = seat(bucket)

            the res is 8.
    """
    slot = {'length': -1, 'bit': -1}
    length = 0
    bit = -1
    counter = 0
    for item in bucket:
        if item:
            if bit != 0:
                length //= 2
                bit += length
            if length > slot['length'] and bit != -1:
                slot['length'] = length
                slot['bit'] = bit
            bit = -1
        else:
            if bit == -1:
                bit = counter
                length = 0
            else:
                length += 1

        counter += 1

    if length > slot['length']:
        slot['length'] = length
        slot['bit'] = counter - 1

    return slot['bit']


if __name__ == '__main__':
    # a = [1, 0, 0,0,0,0]
    # res = seat(a)
    # print(res)
    from redis import Redis
    conn = Redis(host='localhost', password=12345)
    print(conn.get('abc'))

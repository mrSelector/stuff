def main():
    try:
        raise ValueError('Value error')

    except ValueError as error:
        print(error)
        raise


try:
    main()
except ValueError:
    print('error')

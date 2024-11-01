from watchout.get_unicode_info import get_unicode_info


def main():
    # Example usage
    unicode_input = r"\u0937"  # Input Unicode escape format
    unicode_info = get_unicode_info(unicode_input)
    print(unicode_info)


if __name__ == "__main__":
    main()

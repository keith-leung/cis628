import yaml

def read_to_end(filepath: str):
    with open(filepath, encoding="utf8") as f:
        content = f.readlines()
        return content
    return ''


def write_to_file(filepath, content):
    with open(filepath, 'w', encoding="utf8") as f:
        f.write(content)

    return ''

def is_debug_mode():
    with open("config.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        for key, value in data.items():
            if key == 'IsDebug' and bool(value):
                return True

    return False

def get_all_test_cases():
    with open("config.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        for key, value in data.items():
            if key == 'TestCase' and bool(value):
                return value

    return []
def group_advanced_anagrams(words):
    groups = {}

    for word in words: 
        # Create new string for normalized word
        normalized = ""
        for char in word:
            if char.isalpha():
                normalized += char.lower()

        if normalized != "":
            # Create tuple key as sorted letters
            sorted_letters = sorted(normalized)
            key = tuple(sorted_letters)

            # Add into groups dict
            if key not in groups:
                groups[key] = []
            groups[key].append(word) # Append original word

    # Check groups have at least 2 words
    filtered_groups = {}
    for key in groups:
        if len(groups[key]) >= 2:
            # Sort the list of words alphabetically inside group
            sorted_group = sorted(groups[key])
            filtered_groups[key] = sorted_group

    # Create the list of groups: sorted by size descending, then alphabetically
    groups_list = []
    for key in filtered_groups:
        groups_list.append(filtered_groups[key])

    groups_list.sort(key=lambda group: (-len(group), group[0]))

    # Return the tuple
    return (filtered_groups, groups_list)

words = ["characteristics", "tscahriceirast", "scrahticsieta", "anotherword"]
print(group_advanced_anagrams(words))
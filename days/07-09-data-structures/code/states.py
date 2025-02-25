us_state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ',
                   'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
                   'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL',
                   'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
                   'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
                   'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
                   'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
                   'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                   'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE',
                   'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                   'New Mexico': 'NM', 'New York': 'NY',
                   'North Carolina': 'NC', 'North Dakota': 'ND',
                   'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
                   'Pennsylvania': 'PA', 'Rhode Island': 'RI',
                   'South Carolina': 'SC', 'South Dakota': 'SD',
                   'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
                   'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                   'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

# noinspection DuplicatedCode
states = ['Oklahoma', 'Kansas', 'North Carolina', 'Georgia', 'Oregon',
          'Mississippi', 'Minnesota', 'Colorado', 'Alabama',
          'Massachusetts', 'Arizona', 'Connecticut', 'Montana',
          'West Virginia', 'Nebraska', 'New York', 'Nevada', 'Idaho',
          'New Jersey', 'Missouri', 'South Carolina', 'Pennsylvania',
          'Rhode Island', 'New Mexico', 'Alaska', 'New Hampshire',
          'Tennessee', 'Washington', 'Indiana', 'Hawaii', 'Kentucky',
          'Virginia', 'Ohio', 'Wisconsin', 'Maryland', 'Florida',
          'Utah', 'Maine', 'California', 'Vermont', 'Arkansas', 'Wyoming',
          'Louisiana', 'North Dakota', 'South Dakota', 'Texas',
          'Illinois', 'Iowa', 'Michigan', 'Delaware']

NOT_FOUND = 'N/A'


def main():
    print(get_every_nth_state())
    print(get_every_nth_state(n=20))
    print(get_state_abbrev('Oklahoma'))
    print(get_state_abbrev('Washington'))
    print(get_state_abbrev('Whatever'))
    print(get_longest_state(us_state_abbrev))
    print(get_longest_state(states))
    print(combine_state_names_and_abbreviations())


def get_every_nth_state(states=states, n=10):
    """Return a list with every nth item (default argument n=10, so every
       10th item) of the states list above (remember: lists keep order)"""
    result = states[n - 1::n]
    return result


def get_state_abbrev(state_name, us_state_abbrev=us_state_abbrev):
    """Look up a state abbreviation by querying the us_state_abbrev
       dict by full state name, for instance 'Alabama' returns 'AL',
       'Illinois' returns 'IL'.
       If the state is not in the dict, return 'N/A' which we stored
       in the NOT_FOUND constant (takeaway: dicts are great for lookups)"""
    result = us_state_abbrev.get(state_name)
    if result is None:
        return NOT_FOUND

    return result


def get_longest_state(data):
    """Receives data, which can be the us_state_abbrev dict or the states
       list (see above). It returns the longest state measured by the length
       of the string"""
    if type(data) == dict:
        state_dict = {len(state): state for state in data.keys()}
        longest_state = max(state_dict.keys())
        return state_dict[longest_state]
    elif type(data) == list:
        state_dict = {len(state): state for state in data}
        longest_state = max(state_dict.keys())
        return state_dict[longest_state]


def combine_state_names_and_abbreviations(us_state_abbrev=us_state_abbrev,
                                          states=states):
    """Get the first 10 state abbreviations from the (sorted) us_state_abbrev dict,
       and the last 10 states from the (sorted) states list (see also above).
       Combine these two lists into a new list and return it.
       Here is the truncated resulting list (see also the tests):
       ['AK', 'AL', 'AZ', ..., 'West Virginia', 'Wisconsin', 'Wyoming']"""
    sorted_abbrvs = list(us_state_abbrev.values())
    sorted_abbrvs.sort()
    sorted_abbrvs = sorted_abbrvs[:10]

    states.sort()
    sorted_states = states[-10:]
    sorted_abbrvs.extend(sorted_states)
    return sorted_abbrvs


if __name__ == "__main__":
    main()

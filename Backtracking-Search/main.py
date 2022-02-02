import plotly.express as px

# Do not modify the line below.
countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay",
             "Peru", "Suriname", "Uruguay", "Venezuela"]

# Do not modify the line below.
colors = ["blue", "green", "red", "yellow"]

# connections between countries
connections = {
    "Argentina": ["Bolivia", "Brazil", "Chile", "Paraguay", "Uruguay"],
    "Bolivia": ["Argentina", "Brazil", "Chile", "Paraguay", "Peru"],
    "Brazil": ["Argentina", "Bolivia", "Colombia", "Guyana", "Paraguay", "Peru",
               "Suriname", "Uruguay", "Venezuela"],
    "Chile": ["Argentina", "Bolivia", "Peru"],
    "Colombia": ["Brazil", "Ecuador", "Peru", "Venezuela"],
    "Ecuador": ["Colombia", "Peru"], "Falkland Islands": [],
    "Guyana": ["Brazil", "Suriname", "Venezuela"], "Paraguay": ["Argentina", "Bolivia", "Brazil"],
    "Peru": ["Bolivia", "Brazil", "Chile", "Colombia", "Ecuador"], "Suriname": ["Brazil", "Guyana"],
    "Uruguay": ["Argentina", "Brazil"], "Venezuela": ["Brazil", "Colombia", "Guyana"]
}


# Colors the map with choosing colors that every neighbor have a different color.
# Returns dictionary if there is a solution otherwise will return None(Failure)
def backtrack_search(ret, variables, domains, conns):
    # checks that is the algorithm finished
    if check_search(ret, variables, conns):
        return ret
    # picks a country that has no color
    add = get_unassigned_variables(ret, variables)
    # checks possible colors of the chosen country
    for item in get_unassigned_domains(ret, add, conns, domains):
        ret[add] = item
        # calls itself recursively
        result = backtrack_search(ret, variables, domains, conns)
        # if result none then it will check other colors
        if result is not None:
            return result
    # if there is any solution then it will return None
    return None


# checks that is the algorithm finished or not, will return True if it is finished.
def check_search(ret, variables, conns):
    # checks that is there any country that has no color, if it is then will return false
    for item in variables:
        if ret.get(item) is None:
            return False
    # checks that are there any neighbor countries that have the same color, if it is then will return false
    for item in ret.keys():
        for conn_item in conns.get(item):
            if ret.get(item) == ret.get(conn_item):
                return False
    return True  # returns True means the algorithm has the correct solution


# returns one country that has no color
def get_unassigned_variables(ret, variables):
    unassigned = []  # initially empty
    for item in variables:
        if ret.get(item) is None:
            unassigned.append(item)
    if len(unassigned) == 0:  # length is 0 means there is not any unassigned country
        return None
    return unassigned[0]


# returns possible colors of the chosen country(named as variable)
def get_unassigned_domains(ret, variable, conns, domain):
    assigned = []  # initially empty
    if variable is None:
        return assigned  # if country(variable) is null returns empty list
    for item in conns.get(variable):
        if ret.get(item) is not None:
            assigned.append(ret.get(item))
    return get_differences(domain, assigned)  # returns unassigned domains


# returns differences between two lists as a list
def get_differences(domain, assigned):
    return [item for item in domain if item not in assigned]


# colormap should be a dictionary having countries as keys and colors as values.
def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()


# main to call necessary functions
if __name__ == "__main__":
    # coloring test
    # colormap_test = {'Argentina': 'blue', 'Bolivia': 'green', 'Brazil': 'red', 'Chile': 'red', 'Colombia': 'blue',
    #                'Ecuador': 'green', 'Falkland Islands': 'blue', 'Guyana': 'blue', 'Paraguay': 'yellow',
    #               'Peru': 'yellow', 'Suriname': 'green', 'Uruguay': 'green', 'Venezuela': 'green'}

    # calling the algorithm
    color_map = backtrack_search({}, countries, colors, connections)
    print(color_map)
    if color_map is not None:
        plot_choropleth(colormap=color_map)
    else:
        print("Failure!")

    # plot_choropleth(colormap=colormap_test)

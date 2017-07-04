from bandecoapi.cardapio.cardapio import Cardapio


def get_menu(**kwargs):
    """Get Menu

    Fetch menu from Unicamp's servers

    Args:
        menus (list): List of menus to fetch
            Options: breakfast, lunch, veglunch, dinner, vegdinner
        days_delta (int, optional): Fetch menu 'n' days from now
        hours_delta (int, optional): Fetch menu 'n' hours from now
        date (str, optional): Date to fetch menu from (YYYY-mm-dd) - overrides days and hours delta

    Returns:
        dict:
            menu (dict, optional): Menus from the day, if available
            error (str, optional): Error message explaining what went wrong, or if there is no menu for the day
    """

    valid_args = {
        "menus": list,
        "days_delta": int,
        "hours_delta": int,
        "date": str
    }

    menu_options = kwargs.pop("menus", False)
    if not menu_options:
        return {"error": "'menus' é um argumento obrigatório"}

    if type(menu_options) != valid_args["menus"]:
        return {"error": ' '.join(["'menus' tem que ser do tipo", str(valid_args["menus"])])}

    for arg in kwargs:
        if not valid_args.get(arg, False):
            return {"error": " ".join([str(arg), "não é um argumento válido"])}
        if not isinstance(kwargs[arg], valid_args.get(arg)):
            return {"error": " ".join([str(kwargs[arg]), "não é um tipo válido para o argumento", str(arg)])}
    try:
        cardapio = Cardapio(**kwargs)
    except Exception as e:
        return {"error": str(e)}

    response = {}
    for menu in menu_options:
        if not isinstance(menu, str):
            return {"error": "Os valores da lista 'menus' têm que ser strings"}
        response[menu] = getattr(cardapio, menu, False)
        if not response[menu]:
            return {"error": " ".join([str(menu), "não é uma opção menu válida"])}
    return {"menu": response}

# Bandeco API

API to get menus from Unicamp's bandeco

## Install

run `pip install bandecoapi`

## Usage

The main endpoint is the `bandecoapi.api.get_menu` function.

```
bandecoapi.api.get_menu()

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

```

Example:
```Python
>>> from bandecoapi import api
>>> menus = ["breakfast", "lunch"]
>>> days_delta = 2
>>> api.get_menu(menus=menus, days_delta=days_delta)
{'menu': {'lunch': 'Arroz e feijão\nPrato principal: Carne moída nutritiva\nMacarrão alho e óleo\nPts com abóbora seca\nSalada: Acelga\nSobremesa: Melancia\nSuco: Laranja\nObservações: O cardápio contém glúten no pão e no macarrão alho e óleo. Não contém lactose. Informamos que os restaurantes: Ru,ra e rs estão funcionando normalmente. Não esqueça, sua caneca !', 'breakfast': 'Café, leite, pão, margarina, geleia, fruta'}}
```

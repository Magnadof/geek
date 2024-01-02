from operator import index
from selectors import EpollSelector
import pandas as pd
import func
from time import sleep

df = pd.read_excel("banco_animes.xlsx")

while True:
    func.cor(33, "my anime bank")
    try:
        choose = int(
            input(
                """
Welcome to my anime bank, choose an option
                    
[1]see list
[2]Edit                    
[3]Genres
[4]Find
[5]Recommend 
[6]Exit 

"""
            )
        )
        if choose == 1:
            amount_of_anime = df["nome"].count()
            name = df["nome"].to_string(index=False)
            func.cor(32, f"We have a total of {amount_of_anime} anime")
            if amount_of_anime > 0:
                print(name.upper())
            sleep(2)

        elif choose == 2:
            while True:
                func.cor(36, "Edit")
                choose = int(
                    input(
                        """
[1] Register
[2] Remove
[3] Change information
[4] back                                                             
"""
                    )
                )

                if choose == 1:
                    func.cor(36, "Enter the name of the anime:")
                    name = input()
                    name = name.lower()
                    if name in df["nome"].str.lower().values:
                        func.cor(31, "Anime Already Registered")
                        continue
                    else:
                        while True:
                            try:
                                func.cor(32, "Number of episodes:")
                                episodes = int(input())
                                break
                            except:
                                func.cor(31, "must add a numeric value")

                    func.cor(94, "What genre?:")
                    genre = input()
                    func.cor(34, "From a brief description:")
                    description = input()
                    new_anime = pd.DataFrame(
                        {
                            "nome": [name],
                            "eps": [episodes],
                            "genero": [genre],
                            "descrição": [description],
                        }
                    )
                    df = pd.concat([df, new_anime], ignore_index=True)
                    func.cor(
                        34, f"Anime:{name.upper()} has been successfully registered"
                    )

                elif choose == 2:
                    func.cor(93, "Which anime do you want to delete?")
                    name = input()
                    if name in df["nome"].str.lower().values:
                        indice = df.loc[df["nome"].str.lower() == name].index[0]

                        while True:
                            print(
                                f"Are you sure you want to delete {name.upper()}? y/n"
                            )
                            choose = input()
                            choose = choose.lower()
                            if choose == "y":
                                df = df.drop(indice)
                                break
                            elif choose == "n":
                                break
                            else:
                                func.cor(31, "You must answer with Y or N")
                    else:
                        func.cor(93, "Anime Not Found")

                elif choose == 3:
                    func.cor(93, "Which anime do you want to change information ?")
                    name = input()
                    name = name.lower()
                    if name in df["nome"].str.lower().values:
                        while True:
                            try:
                                func.cor(93,f'What you want to change from {name.upper()}?')
                                choose = int(
                                    input(
                                        """
[1] Name
[2] Number of episodes
[3] Gender
[4] Description
[5] back

"""
                                    )
                                )
                                if choose == 1:
                                    temporary_name = input("what name do you want to put?: ")
                                    while True:
                                        choose = input(
                                            f"""Do you want to change the name from {name} to {temporary_name} ? y/n\n""").lower()
                                        if choose == "y":
                                            new_name = df.loc[
                                                df["nome"].str.lower() == name, "nome"
                                            ] = temporary_name
                                            break
                                        elif choose == "n":
                                            break
                                        else:
                                            func.cor(31, "Ivalid value")
                                elif choose == 2:
                                    episodes=None
                                    while True:
                                        try:
                                            episodes = int(input(f"How many episodes does {name} have? " ))
                                            break
                                        except:
                                            func.cor(31, "must add a numeric value")

                                    while True:
                                        choose=input('are you sure that x has y y episodes ? Y/N')
                                        if choose.lower() == 'y':
                                            df.loc[df["nome"] == name, 'eps']=episodes
                                            break
                                        elif choose.lower() == 'n':
                                            break
                                        else:
                                            func.cor(31, "You must answer with Y or N")

                                elif choose == 3:
                                    genera= df.loc[df["nome"]==name,'genero'].values[0]

                                    print(f'\nThe genera of {name} are {genera}\n')



                                elif choose == 4:
                                    pass
                                elif choose == 5:
                                    break
                                else:
                                    func.cor(31, "Ivalid value")

                            except:
                                func.cor(31, "must add a numeric value")
                    else:
                        func.cor(93, "This anime doesn't exist in our database")

                elif choose == 4:
                    break
                else:
                    func.cor(31, "Invalid value")

        elif choose == 3:
            pass
        elif choose == 4:
            pass
        elif choose == 5:
            pass
        elif choose == 6:
            break
        else:
            func.cor(31, "Ivalid value")
    except:
        func.cor(31, "must add a numeric value")

df.to_excel("banco_animes.xlsx", index=False)

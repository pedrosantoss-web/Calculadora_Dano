from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def homer():

    inimigos = [
        {
            "nome": "Feiticeira",
            "vida": 10,
            "foto": "https://i.pinimg.com/736x/c0/ab/36/c0ab36aee058b62c8aaf2624ca5a22dd.jpg"
        },
        {
            "nome": "Orc",
            "vida": 30,
            "foto": "https://pm1.narvii.com/6284/90c5f1d94fef70be09643026c7ec1d7a244fd609_hq.jpg"
        },
        {
            "nome": "Goblin",
            "vida": 45,
            "foto": "https://pm1.narvii.com/6547/497b3625f161b4847a9eb557813023526a339886_hq.jpg"
        }
    ]
    armas = [

        {
            "nome": "Flecha",
            "dano": 30,
            "foto": "https://4.bp.blogspot.com/-qryTAzvIJeI/WYzifDArYwI/AAAAAAAABi4/69XiemrWaJs1jZR7kPwidK2c4PsPqXLvACLcBGAs/w1200-h630-p-k-no-nu/the_evening_huntress_by_leesmith.jpg" 
            
        },
         {
            "nome": "Espada",
            "dano": 50, 
            "foto": "https://i.pinimg.com/originals/8b/af/7f/8baf7f97f7ccf05d4658a61432679404.jpg"
            
        },
         {
            "nome": "Soco",
            "dano": 9,
            "foto": "https://as2.ftcdn.net/jpg/01/22/01/07/500_F_122010713_piAuqtXZe4SwJPlF3UYCLD6BvNYBNv72.jpg" 
            
        }
    ]

    return render_template(
        "index.html",
        inimigos = inimigos,
        armas = armas
    ) 

if __name__ == "__main__":
    app.run(debug=True)       
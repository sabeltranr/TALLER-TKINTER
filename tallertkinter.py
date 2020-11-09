import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import *
from PIL import Image,ImageTk
import tkinter
from tkinter import PhotoImage
from tkinter import *
from PIL import Image,ImageTk
def init_window():

    window = tk.Tk()
    window.title("mi primera aplicacion")
    window.geometry('600x450')
    window.resizable(0,0)

    label= tk.Label(window,text='calculadora',font=('Arial bold',15))
    label.grid(column=0,row=0)

    imagen=PhotoImage(file="numeritos.png")
    fondo2 = Label(window, image=imagen).place(x=-20, y=140)

    ellabel=tk.Label(window,text="NOTAS",font=("calibri",15),fg="red")
    ellabel.place(x=450,y=13)
    texto = Text(window, width=17, height=10)
    texto.place(x=450, y=40)

    def trigo():
        raiz_trigo=Toplevel()
        raiz_trigo.title("valores funciones")
        raiz_trigo.resizable(1, 1)
        raiz_trigo.config(width=700, height=600, bg="blue")

        unframe= Frame(raiz_trigo)
        unframe.pack(fill="y")
        unframe.config(width="450",height="600",bg="white",relief="groove",bd=30)

        imagen1 = PhotoImage(file="trgo.png")
        imagen_trigo = Label(unframe, image=imagen1).place(x=30, y=30)

        def raiz_barra():
            raiz_barra = tk.Tk()
            raiz_barra.title("Un laberinto hacia el mar")
            raiz_barra.geometry('520x450')
            raiz_barra.resizable(0, 0)

            scrollbar = tk.Scrollbar(raiz_barra)
            c = tk.Canvas(raiz_barra, background="gray", yscrollcommand=scrollbar.set)
            scrollbar.config(command=c.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            elframe = tk.Frame(c)
            c.pack(side="left", fill="both", expand=True)
            c.create_window(0, 0, window=elframe, anchor="nw")
            v = """Vivía con su madre y su hermano pequeño en una preciosa aldea de casas blancas con tejados de paja, situada en el sur de Francia. Un lugar lleno de vegetación. Sus habitantes cultivaban lo imprescindible e intercambiaban los excedentes, pues el dinero no existía. Todo era perfecto.
        Todo, excepto un «pequeño» detalle: era imposible salir de allí. La aldea se encontraba en el centro de un laberinto gigante e infranqueable formado por zarzas y espinos.
        Además, se decía, se rumoreaba, que el laberinto crecía, que sus ramificaciones se reproducían, que sus caminos eran más largos y estrechos y que, por tanto, escapar de allí era cada día más difícil.
        Muchos habían muerto buscando la salida. Unos habían sido atravesados por las espinas, otros asfixiados por las ramas de las plantas, que crecían atrapando todo lo que encontraban. Otros morían de sed, perdidos por las sinuosas sendas.
        Charles acababa de cumplir 12 años y vivía con su madre y su hermano pequeño en una bonita cárcel.
        Un medallón de latón fue su regalo de aniversario. Un medallón que su madre había heredado de su padre, y éste a su vez, de su madre. Había pasado de generación en generación y ahora había llegado a manos de Charles. ¡Quién sabe cuántos años tendría! Era una reliquia de su familia, un imperfecto disco metálico demasiado pesado y grande para su pequeño cuello. Pendía de una tosca cadena, más pesada todavía.
        Pero con doce años no quieres medallones, ni de oro ni de plata: quieres libertad, quieres salir y entrar, ser independiente, pasar inadvertido, conocer, investigar, probar. Un medallón con una pesada cadena es un símbolo más de tu encierro y detención.  Y esto fue lo que Charles pensó, intentando que su madre no notara su descontento.
        Así que guardó su regalo debajo de el colchón y retomó su lectura. Los libros eran el único referente para los habitantes de la aldea. Entre sus páginas se podían encontrar dibujos de montañas, de valles, de animales y de plantas. Eran libros preciosos, maravillosos, misteriosos.
        Charles leyó todos los textos que encontró. Aprendió muchas cosas, descubrió imágenes de las olas del mar, de animales increíbles y de plantas con propiedades curativas.
        Su fantasía se desataba: soñaba con glaciares que se derriten creando enormes lagos, imaginaba lagos de los que nacen límpidos riachuelos y dibujaba ríos que desembocan en el mar. Su inconsciente siempre le conducía hacia el mismo sitio: la búsqueda de la libertad. Y para él el mar representaba la libertad.
        Y entre sueño y sueño, Charles sacaba el medallón de sus antepasados, lo observaba y lo limpiaba, deseando que ese metal le transmitiera propiedades mágicas para poder salir de allí. Pero la magia no llegaba. Leía y releía las inscripciones que algún antepasado suyo había grabado en el anverso y reverso de la medalla, 
        el niño avanza sin pensar hacia lo desconocido
        el joven, a veces, retrocede para evolucionar
        el adulto busca nuevos retos
        el anciano se convierte de nuevo en niño
        pero no conseguía comprender el significado de esas palabras.
        Lo que sí comprendió es que su hermano estaba enfermo.
        Con 12 años y siete meses, Charles tomó una determinación: se internaría entre las zarzas. Si había un mar, estaba fuera; si había más libros, estaban fuera; si había cura para su hermano pequeño, estaba fuera. Al amanecer, dejando una nota de despedida, salió con su hatillo y su medallón hacia el interior del horrible laberinto.

        Había pensado mucho en cómo sería adentrarse en esa locura de pasillos y cruces. Tenía claro que debía seguir una estrategia, trazar un plan. Por supuesto, había que marcar los cruces visitados y la dirección tomada. Esto no parecía muy difícil, podían hacerse marcas. Por ejemplo, atando a las plantas trozos de tela de distintos colores, indicando si ese lugar ya había sido visitado y en qué dirección se había recorrido. Tela azul en el comienzo de un camino, tela roja al final.
        Charles comenzó marcando las sendas de esta forma, con mucha paciencia y disciplina. Un error podía ser mortal. Pero aún así, la cosa estaba muy complicada. Llegó un momento en que empezó a ver lazos azules y rojos por todas partes, que indicaban que ya había estado allí. A veces tenía la impresión de estar dando vueltas. Y pasadas varias horas corroboró que estaba perdido del todo.
        Las zarzas iban dejando huellas en sus piernas, brazos y cara, raspones por todo su cuerpo. Luego comenzaron los mareos, la sensación de agobio al saberse desorientado. Pasaba por los mismos sitios una y otra vez y no era capaz de regresar a su casa ni de salir de esa cárcel  Su cabeza daba vueltas, parecía que le faltaba el oxígeno.
        Entonces se acordó de el medallón. Palpó sus inscripciones, que tantas veces había leído:
        el niño avanza sin pensar hacia lo desconocido
        el joven, a veces, retrocede para evolucionar
        el adulto busca nuevos retos
        el anciano se convierte de nuevo en niño
        y con su mente nublada por el mareo y la confusión, en un estado casi de trance, lo comprendió:  esas inscripciones eran un algoritmo para salir de allí.
        El niño, el joven, el adulto y el anciano representaban a los pasillos. Un pasillo que se recorre por primera vez es un niño. Si lleva a un lugar en el que se ha estado con anterioridad, se convierte en joven. Un camino que se ha recorrido en los dos sentidos, es un adulto; y un camino que lleva a un lugar que ha sido totalmente explorado es un anciano. Pensando en todo esto, consiguió descifrar el mensaje oculto entre las palabras de la medalla.
        Charles bebió un poco de agua, recobró fuerzas y, sobre todo, recuperó la esperanza.  Por supuesto, seguía marcando con cinta roja o azul los comienzos y finales de los pasillos. Pero ahora sabía que tenía que elegir muy bien el camino a tomar en función de la combinación de colores de los lazos encontrados en los cruces.
        Consiguió salir de el bucle en el que había estado tanto tiempo. Tuvo que pasar por callejones cada vez más estrechos y punzantes, llenos de bifurcaciones. En ocasiones debía retroceder sobre sus pasos. Cuando tenía dudas, tocaba el medallón para volver a interpretar sus mensajes. Éste se había convertido para él en un amuleto que representaba su salvación, una fuente de inspiración y de energía. A veces era muy complicado elegir el camino adecuado.
        Exhausto y herido, con la cara ensangrentada y los labios resecos, tres días más tarde vio, por fin, la salida de ese horrible, tenebroso y siniestro laberinto.
        A pesar de sus escasas fuerzas, caminó deprisa los últimos metros de oscura senda hasta llegar a la anhelada puerta.
        Lo que vio entonces le pareció un milagro. Ahora tenía ante sí una verde pradera rodeada de nevadas montañas y un cielo azul. No muy lejos, había un pequeño riachuelo que, tarde o temprano, desembocaría en el mar.
        Gracias a su audacia e intuición, había conseguido ser libre.   
        Tomado de: https://aprendiendomatematicas.com/cuento-matematico-laberinto/"""



            texto = tk.Label(elframe, wraplength=500, text=v, background="pink4")
            texto.pack()
            raiz_barra.update()
            c.config(scrollregion=c.bbox("all"))
            raiz_barra.mainloop()

        boton_cuento = tkinter.Button(unframe, text="cuento",
                                      bg="pink4",
                                      fg="White",
                                      font=("Calibri", 15),
                                      command=lambda: raiz_barra())
        boton_cuento.place(x=0, y=500)

        def mensaje():
            respuesta = messagebox.askquestion("Cerrar", "¿seguro que desea cerrar?")
            if (respuesta == "yes"):
                raiz_trigo.destroy()

        boton_salir=tkinter.Button(unframe,text="Salir",
                                   bg="red",
                                   fg="White",
                                   font=("Calibri",15),
                                    command=lambda :mensaje())
        boton_salir.place(x=340,y=500)


        raiz_trigo.mainloop()



    fondo_boton4 = Image.open('table.png')
    fondo_boton4 = fondo_boton4.resize((100, 80), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
    fondo_boton4 = ImageTk.PhotoImage(fondo_boton4)
    boton4 = tkinter.Button(window,
                            image=fondo_boton4,
                            text="TRIGONOMETRIA",
                            compound="top",
                            bg='white',
                            fg='black',
                            font=("Calibri", 11),
                            command=lambda : trigo()
                            )
    boton4.place(x=470, y=300)

    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)

    entrada1.grid(column=1, row=1)
    entrada2.grid(column=1, row=2)

    label_entrada1 = tk.Label(window, text='Ingrese primer numero', font=('Arial bold', 10))
    label_entrada1.grid(column=0, row=1)
    label_entrada2 = tk.Label(window, text='Ingrese segundo numero', font=('Arial bold', 10))
    label_entrada2.grid(column=0, row=2)

    label_operador = tk.Label(window, text='escoja un operador', font=('Arial bold', 10))
    label_operador.grid(column=0, row=3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores["values"] = ["+", "-", "*", "/", "pow","porcentaje","√"]
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=3)

##
    label_resultado = tk.Label(window,text="Resultado: ",font=('Arial bold',15))
    label_resultado.grid(column=0,row=5)

    def calculadora(num1,num2,operador):
        if operador=="+":
            resultado = num1+ num2
        elif operador =="-":
            resultado = num1 - num2
        elif operador =="*":
            resultado = num1 * num2
        elif operador=="√":
            resultado = num1 ** (1/num2)
        elif operador =="/":
            resultado = round(num1 / num2,4)
        elif operador == "porcentaje":
            resultado = ((num1/100)*num2)
        
        else:
            resultado=num1**num2
        return resultado

    def click_calcular(label,num1,num2,operador):
        valor1= float(num1)
        valor2=float(num2)

        res=calculadora(valor1,valor2,operador)

        label.configure(text="Resultado: "+str(res))

    boton=tk.Button(window,
                    command = lambda:click_calcular(
                            label_resultado,
                            entrada1.get(),
                            entrada2.get(),
                            combo_operadores.get()),
                    text="calcular",
                    bg = "orange",
                    fg="green")
    boton.grid(column=1,row=5)
    window.mainloop()

def main():
    init_window()
main()
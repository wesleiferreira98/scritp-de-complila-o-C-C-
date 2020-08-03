#! /bin/bash
comexe(){
	g++ "$prog".cpp -o"$prog"

  	if [  -f "$prog"  ];
  		then
   		./"$prog"
  	fi
}
clear
echo "Digite o nome do programa: "
read prog
if [  -f "$prog"  ];
  then
   rm "$prog"
fi

if [  -f "$prog".cpp  ];
	then
  		comexe

else
  while [ ! -f "$prog".cpp ];
    do
      clear
      echo " O programa $prog.cpp não foi encontrado, por favor digite o nome correto: "
      read prog
      if [  -f "$prog".cpp  ];
        then

       comexe
      fi
    done
fi

 while [ ! -f "$prog" ];
    do
      
      echo " O programa $prog.cpp não foi encontrado ou está com erros, por favor tente novamente: "
      read prog
      if [  -f "$prog".cpp  ];
        then

        comexe
      fi
done
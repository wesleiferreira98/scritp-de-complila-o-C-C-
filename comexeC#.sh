#! /bin/bash
comexe(){
  mcs "$prog".cs
  if [  -f "$prog".exe  ];
      then
        mono "$prog".exe
  fi
}
clear
echo "Digite o nome do programa: "
read prog
if [  -f "$prog".exe  ];
  then
   rm "$prog".exe
fi

if [ -f "$prog".cs ]
  then
   comexe

else
  while [  ! -f "$prog".cs  ];
    do
      clear
      echo " O programa $prog.cs não foi encontrado por favor digite o nome correto: "
      read prog

      if [ -f "$prog".cs ]
        then
         comexe
      fi
    done
fi

while [  ! -f "$prog".exe  ];
    do
      
      echo " O programa $prog.cs está com erros ou não foi encontrado,  por favor conserte e tente novamente: "
      read prog

      if [ -f "$prog".cs ];
        then
          comexe
      fi
done

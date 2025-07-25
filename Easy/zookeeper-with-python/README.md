# 🦁 Zookeeper

A step-by-step Python project simulating a virtual zoo. Each stage introduces new concepts, from printing text to handling user input and managing data.

---

## ✅ Tasks Overview

This project is divided into multiple tasks. Each task builds upon the previous one to incrementally simulate a zoo management system.

---

<details>
<summary><strong>📌 Task 1 – Print Animal Status</strong></summary>

### 📝 Description

To start, you'll build a simple console program that prints the current status of the animals in your virtual zoo.

### 🎯 Objectives

- Print a few lines of text exactly as shown in the example.

### 💡 Example Output

```
I love animals!\
Let's check on the animals...\
The deer looks fine.\
The bat looks happy.\
The lion looks healthy.
```
</details>

---

<details>
    <summary><strong>📌 Task 2 – Display the Camel</strong></summary>

### 📝 Description

One of the most important parts of working with animals is observing them. Now it’s time to show the animals on screen — let’s start by printing an ASCII image of a camel.

### 🎯 Objectives

- Store the camel ASCII image in a variable called `camel`, using a **raw triple-quoted string** (`r""" ... """`);

### 💡 Example Output

```
Switching on the camera in the camel habitat...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Look at that! Our little camel is sunbathing!

```

</details>

---

<details>
<summary><strong>📌 Task 3 – Show Habitat by User Input</strong></summary>

### 📝 Description

Now it’s time to make your program interactive! It should ask the user which habitat they want to view and display the corresponding animal.

The program uses a predefined list called `animals`, where each item is an ASCII image string for a specific habitat. The input number corresponds to the index in this list.

### 🎯 Objectives

1. Prompt the user with the following message:  
   `Please enter the number of the habitat you would like to view:`

2. Use the input as an index to access and print the corresponding animal from the list;

3. After displaying the animal, print the final message:

	`You've reached the end of the program. To check another habitat, please restart the watcher.`

### 💡 Example Output

```
Please enter the number of the habitat you would like to view: > 5

Switching on the camera in the rabbit habitat...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
It looks like we will soon have more rabbits!
---
You've reached the end of the program. To check another habitat, please restart the watcher.
```

---

<details>
<summary><strong>📌 Task 4 – Loop Until Exit</strong></summary>

### 📝 Description

Your program is now becoming more interactive. In this stage, users can view multiple habitats without restarting the program. The interaction continues in a loop until the user decides to exit.

### 🎯 Objectives

1. Repeat the behavior from the previous task in a **loop**;
2. Prompt the user each time with:  
   `Please enter the number of the habitat you would like to view:`
3. If the user types `exit`, the program ends;
4. After exiting, print:  
   `See you later!`

### 💡 Example Session (simplified)

```
Please enter the number of the habitat you would like to view: > 3

Switching on the camera in the goose habitat...

                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \
 <_  `     (  <`<            \              `-._\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
The goose is staring intently at you... Maybe it's time to change the channel?
Please enter the number of the habitat you would like to view: > 1

Switching on the camera in the lion habitat...
                                               ,w.
                                             ,YWMMw  ,M  ,
                        _.---.._   __..---._.'MMMMMw,wMWmW,
                   _.-""        '''           YP"WMMMMMMMMMb,
                .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
           /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
          /  .'             /  (       .'  /     Ww._     `.  `"
         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
        (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
The lion is roaring!
Please enter the number of the habitat you would like to view: > exit
See you later!
```


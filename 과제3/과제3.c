#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int isSameAccount(char* str1, char* str2) {
    int i = 0;
    while (str1[i] != '\0' || str2[i] != '\0') {
        if (str1[i] != str2[i]) return 0; 
        i++;
    }
    return 1; 
}

void deposit(int* balance, int amount) {
    if (amount > 0) {
        *balance += amount;
        printf("Deposit complete. New balance: $%d\n", *balance);
    }
    else {
        printf("Invalid amount.\n");
    }
}

void withdraw(int* balance, int amount) {
    if (*balance >= amount) {
        *balance -= amount;
        printf("Withdrawal complete. New balance: $%d\n", *balance);
    }
    else {
        printf("Insufficient funds.\n");
    }
}

void transfer(int* sendBal, int* recvBal, int amount) {
    if (*sendBal >= amount) {
        *sendBal -= amount;
        *recvBal += amount;
        printf("Transfer complete. Your balance: $%d\n", *sendBal);
    }
    else {
        printf("Transfer failed due to insufficient funds.\n");
    }
}

int main() {
    char accounts[3][20] = { "111-001", "111-002", "111-003" };
    int passwords[3] = { 1234, 5678, 9999 };
    int balances[3] = { 10000, 50000, 0 };

    char inputAcc[20];
    int inputPw, userIdx = -1;

    printf("Login\n");
    printf("account?: "); 
    scanf("%s", inputAcc);
    printf("password?: "); 
    scanf("%d", &inputPw);

    for (int i = 0; i < 3; i++) {
        if (isSameAccount(accounts[i], inputAcc) && passwords[i] == inputPw) {
            userIdx = i;
            break;
        }
    }

    if (userIdx == -1) {
        printf("Authentication failed.\n");
        return 0;
    }

    int choice = -1;
    while (choice != 0) {
        printf("\n[Logged in: %s | Balance: $%d]\n", accounts[userIdx], balances[userIdx]);
        printf("0.Exit 1.Deposit  2.Withdraw  3.Transfer :");
        scanf("%d", &choice);

        int amount, targetIdx = -1;
        char targetAcc[20];

        if (choice == 1) {
            printf("Enter deposit amount:"); 
            scanf("%d", &amount);
            deposit(&balances[userIdx], amount);
        }
        else if (choice == 2) {
            printf("Enter withdrawal amount:"); 
            scanf("%d", &amount);
            withdraw(&balances[userIdx], amount);
        }
        else if (choice == 3) {
            printf("Enter recipient's account:"); 
            scanf("%s", targetAcc);
            for (int i = 0; i < 3; i++) {
                if (isSameAccount(accounts[i], targetAcc)) {
                    targetIdx = i;
                }
            }
            if (targetIdx != -1 && targetIdx != userIdx) {
                printf("Enter transfer amount:"); 
                scanf("%d", &amount);
                transfer(&balances[userIdx], &balances[targetIdx], amount);
            }
            else {
                printf("Error. Invalid account.\n");
            }
        }
        else if (choice == 0) {
            printf("Closing program...\n");
        }
        else {
            printf("Invalid selection.\n");
        }
    }

    return 0;
}
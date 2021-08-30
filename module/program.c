
#include <stdio.h>
#include <Windows.h>
#include <string.h>
#include <locale.h>

BOOL CALLBACK EnumWindowsProc(HWND hwnd, LPARAM lparam) {
    wchar_t** programs = (wchar_t**) lparam;
    static int index = 0;

    // 여러번 실행 시, static 변수의 값 유지에 의한 오류 방지
    if(getArrayLength(programs) == 0) {
        index = 0;
    }
    
    if(hwnd != NULL) {
        if(IsWindowVisible(hwnd) == 1) {
            wchar_t* program = (wchar_t*)malloc(sizeof(wchar_t) * 1000);
            
            _wsetlocale(LC_ALL, L"korean");

            GetWindowTextW(hwnd, (LPWSTR) program, 1000);

            if(wcslen(program) != 0) {
                programs[index++] = program;  
            }
        }
    }

    return TRUE;
}

__declspec(dllexport) wchar_t** getVisiableProgram() {
    wchar_t** programs = (wchar_t**)malloc(sizeof(wchar_t*) * 20);

    for(int i=0; i<20; i++) {
        programs[i] = NULL;
    }
    
    EnumWindows((WNDENUMPROC) EnumWindowsProc, (LPARAM) programs);

    return programs;
}

__declspec(dllexport) int getArrayLength(wchar_t** arr) {
    int index = 0;
    
    while(arr[index] != NULL) {
        index++;
    }

    return index;
}

__declspec(dllexport) void freeArray(wchar_t** arr) {
    for(int i=0; i<getArrayLength(arr); i++) {
        free(arr[i]);
    }

    free(arr);
}
#include <pybind11/pybind11.h>
#include <string>

namespace py = pybind11;

int connector(const std::string &a, float b) {
    int c = int(b * 100);  // confidence scaled 0-100

    if (a == "happy" || a == "joy") {
        if(c >= 90) return 1;
        else if(c >= 70) return 2;
        else if(c > 60) return 3;
        else if(c > 50) return 4;
        else if(c > 30) return 5;
        else return 6;
    }
    else if(a == "excited") {
        if(c >= 90) return 7;
        else if(c >= 70) return 8;
        else return 9;
    }
    else if(a == "surprise") {
        if(c >= 80) return 10;
        else return 11;
    }
    else if(a == "anger") {
        if(c >= 70) return 12;
        else return 13;
    }
    else if(a == "sadness") {
        if(c >= 60) return 14;
        else return 15;
    }
    else if(a == "fear") {
        return 16;
    }
    else if(a == "disgust") {
        return 17;
    }
    else if(a == "confused") {
        return 18;
    }
    else if(a == "neutral") {
        return 19;
    }

    return -1; // unknown
}


PYBIND11_MODULE(esp32_module, m) {
    m.def("connector", &connector, "Fast emotion");
}

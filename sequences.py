{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyONaCRzoinkFcGVIi7lY6sg"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "NP8hVBsKQQ9T",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1eca7775-cb04-4592-9314-28fb1cb9d954"
      },
      "source": [
        "import numpy as np\n",
        "import math\n",
        "#for i in range(0,4):\n",
        " # print(i)\n",
        "\n",
        "#n=1\n",
        "#m=1\n",
        "#for k in range(0,10):\n",
        " #   n = n + m \n",
        "  #  print(n)\n",
        "   # m = n + m\n",
        "    #print(m)\n",
        "\n",
        "\n",
        "\n",
        "n = 1\n",
        "m=0\n",
        "while n < 6:\n",
        "  n = n+1\n",
        "  m=n+m\n",
        "print(m)\n",
        "\n",
        "\n",
        "# Calcular la suma de 1/(n+1) + 1/(n+2)+ 1/(n+3)+ 1/(n+4)+...1/3n\n",
        "\n",
        "\n",
        "\n",
        "  \n"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from fractions import Fraction\n",
        "\n",
        "n = 2\n",
        "m =0\n",
        "while n < 2*89:\n",
        "  n = n+1\n",
        "  m = 1/n+m\n",
        "print(m)  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nbUISDG2vHt8",
        "outputId": "6717c68f-7e92-4dd7-c8dd-a64d0cbd9d22"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4.261805573826669\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "LTJtdup3zkVZ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
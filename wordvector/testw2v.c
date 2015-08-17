//  Copyright 2013 Google Inc. All Rights Reserved.
//
//  Licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <malloc.h>

const long long max_size = 2000;         // max length of strings
const long long N = 100;                  // number of closest words that will be shown
const long long max_w = 50;              // max length of vocabulary entries

/*int checkword(char* W,char* word)
{
    int i = 0;
    for(i = 0; i < 24415; i++)
    {
        if(!strcmp(W[i],word)) return 1;
    }
    return 0;
}*/
int main(int argc, char **argv) {
  FILE *f;
  char st1[max_size];
  char *bestw[N];
  char file_name[max_size], st[100][max_size];
  float dist, len, bestd[N], vec[max_size];
  long long words, size, a, b, c, d, cn, bi[100];
  char ch;
  float *M,*W;
  char *vocab;
  //modify init
  FILE *f_syn,*f_word;
  float *M_syn1;
  char syn1_name[max_size],word_file[max_size];
  long long syn_words, syn_size;
  if (argc < 3) {
    printf("Usage: ./distance <FILE_syn0> <FILE_syn1> \nwhere FILE contains word projections in the BINARY FORMAT\n");
    return 0;
  }
  strcpy(file_name, argv[1]);
  f = fopen(file_name, "rb");
  if (f == NULL) {
    printf("Syn0 file not found\n");
    return -1;
  }
  //load word file
  strcpy(word_file, argv[3]);
  f_word = fopen(word_file, "r");
  if (f_word == NULL) {
    printf("Word file not found\n");
    return -1;
  }
  //syn1 read
  strcpy(syn1_name, argv[2]);
  f_syn = fopen(syn1_name, "rb");
  if (f_syn == NULL) {
    printf("Syn1 file not found\n");
    return -1;
  }
  fscanf(f_syn, "%lld", &syn_words);
  fscanf(f_syn, "%lld", &syn_size);
  //finish syn1
  fscanf(f, "%lld", &words);
  fscanf(f, "%lld", &size);
  vocab = (char *)malloc((long long)words * max_w * sizeof(char));
  for (a = 0; a < N; a++) bestw[a] = (char *)malloc(max_size * sizeof(char));
  M = (float *)malloc((long long)words * (long long)size * sizeof(float));
  if (M == NULL) {
    printf("Cannot allocate memory: %lld MB    %lld  %lld\n", (long long)words * size * sizeof(float) / 1048576, words, size);
    return -1;
  }
  //load syn1 vector
  M_syn1 = (float *)malloc((long long)syn_words * (long long)syn_size * sizeof(float));
  if (M_syn1 == NULL) {
    printf("Cannot allocate memory: %lld MB    %lld  %lld\n", (long long)syn_words * syn_size * sizeof(float) / 1048576,syn_words, syn_size);
    return -1;
  }
  W = (char *)malloc(24415 * max_w * sizeof(char));
  if (W == NULL) {
    printf("Cannot allocate memory\n");
    return -1;
  }
  int num = 0;
  char ss[max_w];
  for(num = 0; num < 24415; num++)
  {
    fgets(&W[num],max_w,f_word);
    //printf("%s",W[num]);
  }
  /*while(!eof(f_word))
  {
  }*/
  for (b = 0; b < words; b++) {
    a = 0;
    while (1) {
      vocab[b * max_w + a] = fgetc(f);
      if (feof(f) || (vocab[b * max_w + a] == ' ')) break;
      if ((a < max_w) && (vocab[b * max_w + a] != '\n')) a++;
    }
    vocab[b * max_w + a] = 0;
    for (a = 0; a < size; a++) fread(&M[a + b * size], sizeof(float), 1, f);
    len = 0;
    for (a = 0; a < size; a++) len += M[a + b * size] * M[a + b * size];
    len = sqrt(len);
    for (a = 0; a < size; a++) M[a + b * size] /= len;
  }
  //syn1neg vector load
  for (b = 0; b < syn_words; b++) {
    a = 0;
    for (a = 0; a < size; a++) fread(&M_syn1[a + b * size], sizeof(float), 1, f_syn);
    len = 0;
    for (a = 0; a < size; a++) len += M_syn1[a + b * size] * M_syn1[a + b * size];
    len = sqrt(len);
    for (a = 0; a < size; a++) M_syn1[a + b * size] /= len;
  }
  fclose(f);
  fclose(f_syn);
  fclose(f_word);
  while (1) {
    for (a = 0; a < N; a++) bestd[a] = 0;
    for (a = 0; a < N; a++) bestw[a][0] = 0;
    printf("Enter word or sentence (EXIT to break): ");
    a = 0;
    while (1) {
      st1[a] = fgetc(stdin);
      if ((st1[a] == '\n') || (a >= max_size - 1)) {
        st1[a] = 0;
        break;
      }
      a++;
    }
    if (!strcmp(st1, "EXIT")) break;
    cn = 0;
    b = 0;
    c = 0;
    while (1) {
      st[cn][b] = st1[c];
      b++;
      c++;
      st[cn][b] = 0;
      if (st1[c] == 0) break;
      if (st1[c] == ' ') {
        cn++;
        b = 0;
        c++;
      }
    }
    cn++;
    for (a = 0; a < cn; a++) {
      for (b = 0; b < words; b++) if (!strcmp(&vocab[b * max_w], st[a])) break;
      //printf("!!!%s\n",b);
      if (b == words) b = -1;
      bi[a] = b;
      printf("\nWord: %s  Position in vocabulary: %lld\n", st[a], bi[a]);
      if (b == -1) {
        printf("Out of dictionary word!\n");
        break;
      }
    }
    if (b == -1) continue;
    printf("\n                                              Word       Cosine distance\n------------------------------------------------------------------------\n");
    for (a = 0; a < size; a++) vec[a] = 0;
    for (b = 0; b < cn; b++) {
      if (bi[b] == -1) continue;
      for (a = 0; a < size; a++) 
        vec[a] += M[a + bi[b] * size];
    }
    len = 0;
    for (a = 0; a < size; a++) len += vec[a] * vec[a];
    len = sqrt(len);
    for (a = 0; a < size; a++) vec[a] /= len;
    for (a = 0; a < N; a++) bestd[a] = -1;
    for (a = 0; a < N; a++) bestw[a][0] = 0;
    for (c = 0; c < words; c++) {
      a = 0;
      for (b = 0; b < cn; b++) if (bi[b] == c) a = 1;
      if (a == 1) continue;
      dist = 0;
      //if(checkword(W,vocab[c]) == 1)  
        // break;
      for (a = 0; a < size; a++) dist += vec[a] * M_syn1[a + c * size];
      for (a = 0; a < N; a++) {
        if (dist > bestd[a]) {
          for (d = N - 1; d > a; d--) {
            bestd[d] = bestd[d - 1];
            strcpy(bestw[d], bestw[d - 1]);
          }
          bestd[a] = dist;
          strcpy(bestw[a], &vocab[c * max_w]);
          break;
        }
      }
    }
    for (a = 0; a < N; a++) printf("%50s\t\t%f\n", bestw[a], bestd[a]);
  }
  return 0;
}

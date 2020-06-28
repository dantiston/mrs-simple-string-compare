#!/usr/bin/env python3

import unittest

from compare import compare

class CompareTests(unittest.TestCase):

    def setUp(self):
        # See https://github.com/delph-in/pydelphin/blob/develop/tests/mrs_test.py
        self.m1 = "[ LTOP: h0 INDEX: e2 [ e SF: prop TENSE: pres MOOD: indicative PROG: - PERF: - ] RELS: < [ _rain_v_1<3:9> LBL: h1 ARG0: e2 ] > HCONS: < h0 qeq h1 > ICONS: < > ]"
        self.m1b = "[ LTOP: h0 INDEX: e2 [ e SF: prop TENSE: pres MOOD: indicative PROG: - PERF: - ] RELS: < [ _rain_v_1<0:6> LBL: h1 ARG0: e2 ] > HCONS: < h0 qeq h1 > ICONS: < > ]"
        self.m1c = "[ LTOP: h0 INDEX: e2 [ e SF: prop TENSE: past MOOD: indicative PROG: - PERF: - ] RELS: < [ _rain_v_1<3:9> LBL: h1 ARG0: e2 ] > HCONS: < h0 qeq h1 > ICONS: < > ]"
        self.m1d = "[ LTOP: h0 INDEX: e2 [ e SF: prop TENSE: pres MOOD: indicative PROG: - PERF: - ] RELS: < [ _rain_v_1<3:9> LBL: h1 ARG0: e2 ] > HCONS: < > ICONS: < > ]"
        self.m1e = "[ LTOP: h1 INDEX: e2 [ e SF: prop TENSE: pres MOOD: indicative PROG: - PERF: - ] RELS: < [ _rain_v_1<3:9> LBL: h1 ARG0: e2 ] > HCONS: < > ICONS: < > ]"
        self.m1f = "[ LTOP: h0 INDEX: e2 [ e SF: prop TENSE: pres MOOD: indicative PROG: - PERF: - ] RELS: < [ _snow_v_1_rel<3:9> LBL: h1 ARG0: e2 ] > HCONS: < h0 qeq h1 > ICONS: < > ]"
        self.m1g = "[ LTOP: h0 INDEX: e2 [ e SF: prop TENSE: pres MOOD: indicative PROG: - PERF: - ] RELS: < [ _rain_v_1<3:9> LBL: h1 ARG0: e2 ARG1: i6 ] > HCONS: < h0 qeq h1 > ICONS: < > ]"
        self.m2 = "[ LTOP: h0 INDEX: e2 [ e SF: prop TENSE: past MOOD: indicative PROG: - PERF: - ] RELS: < [ _the_q<0:3> LBL: h4 ARG0: x3 [ x PERS: 3 NUM: pl IND: + ] RSTR: h5 BODY: h6 ]  [ _dog_n_1<4:8> LBL: h7 ARG0: x3 ]  [ _chase_v_1<9:15> LBL: h1 ARG0: e2 ARG1: x3 ARG2: x8 [ x PERS: 3 NUM: sg IND: + ] ]  [ _the_q<16:19> LBL: h9 ARG0: x8 RSTR: h10 BODY: h11 ]  [ _dog_n_1<20:24> LBL: h12 ARG0: x8 ] > HCONS: < h0 qeq h1 h5 qeq h7 h10 qeq h12 > ICONS: < > ]"
        self.m2b = "[ LTOP: h0 INDEX: e2 [ e SF: prop TENSE: past MOOD: indicative PROG: - PERF: - ] RELS: < [ _the_q<0:3> LBL: h4 ARG0: x3 [ x PERS: 3 NUM: pl IND: + ] RSTR: h5 BODY: h6 ]  [ _dog_n_1<4:8> LBL: h7 ARG0: x3 ]  [ _chase_v_1<9:15> LBL: h1 ARG0: e2 ARG1: x3 ARG2: x8 [ x PERS: 3 NUM: pl IND: + ] ]  [ _the_q<16:19> LBL: h9 ARG0: x8 RSTR: h10 BODY: h11 ]  [ _dog_n_1<20:25> LBL: h12 ARG0: x8 ] > HCONS: < h0 qeq h1 h5 qeq h7 h10 qeq h12 > ICONS: < > ]"
        self.m3 = "[ LTOP: h0 INDEX: e2 [ e SF: prop TENSE: past MOOD: indicative PROG: - PERF: - ] RELS: < [ _a_q<0:1> LBL: h4 ARG0: x3 [ x PERS: 3 NUM: sg IND: + ] RSTR: h5 BODY: h6 ]  [ _dog_n_1<2:5> LBL: h7 ARG0: x3 ]  [ _bark_v_1<6:13> LBL: h1 ARG0: e2 ARG1: x3 ] > HCONS: < h0 qeq h1 h5 qeq h7 > ICONS: < > ]"
        self.m3b = "[ LTOP: h0 INDEX: e2 [ e SF: prop TENSE: past MOOD: indicative PROG: - PERF: - ] RELS: < [ _bark_v_1<6:13> LBL: h1 ARG0: e2 ARG1: x3 ]  [ _dog_n_1<2:5> LBL: h7 ARG0: x3 ]  [ _a_q<0:1> LBL: h4 ARG0: x3 [ x PERS: 3 NUM: sg IND: + ] RSTR: h5 BODY: h6 ] > HCONS: < h0 qeq h1 h5 qeq h7 > ICONS: < > ]"
        self.m3c = "[ LTOP: h42 INDEX: e7 [ e SF: prop TENSE: past MOOD: indicative PROG: - PERF: - ] RELS: < [ _a_q<0:1> LBL: h11 ARG0: x17 [ x PERS: 3 NUM: sg IND: + ] RSTR: h19 BODY: h30 ]  [ _dog_n_1<2:5> LBL: h7 ARG0: x17 ]  [ _bark_v_1<6:13> LBL: h113 ARG0: e7 ARG1: x17 ] > HCONS: < h42 qeq h113 h19 qeq h7 > ICONS: < > ]"
        self.pathological1 = """[ LTOP: h0 INDEX: e2 [ e SF: prop TENSE: pres MOOD: indicative PROG: - PERF: - ] RELS: < [ _dog_v_1<0:4> LBL: h1 ARG0: e4 [ e SF: prop TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: i3 ARG2: x5 [ x PERS: 3 ] ]  [ _and_c<5:8> LBL: h1 ARG0: e2 ARG1: e4 ARG2: e6 [ e SF: prop TENSE: pres MOOD: indicative PROG: - PERF: - ] ]  [ _dog_v_1<9:13> LBL: h1 ARG0: e6 ARG1: i3 ARG2: x5 ]  [ udef_q<14:57> LBL: h7 ARG0: x5 RSTR: h8 BODY: h9 ]  [ compound<14:57> LBL: h10 ARG0: e11 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: x5 ARG2: x12 [ x IND: + PT: notpro ] ]  [ udef_q<14:19> LBL: h13 ARG0: x12 RSTR: h14 BODY: h15 ]  [ _chase_n_1<14:19> LBL: h16 ARG0: x12 ]  [ udef_q<20:33> LBL: h17 ARG0: x18 [ x PERS: 3 ] RSTR: h19 BODY: h20 ]  [ udef_q<20:24> LBL: h21 ARG0: x22 [ x PERS: 3 NUM: pl IND: + ] RSTR: h23 BODY: h24 ]  [ _dog_n_1<20:24> LBL: h25 ARG0: x22 ]  [ udef_q<25:33> LBL: h26 ARG0: x27 [ x PERS: 3 NUM: pl IND: + ] RSTR: h28 BODY: h29 ]  [ _and_c<25:28> LBL: h30 ARG0: x18 ARG1: x22 ARG2: x27 ]  [ _dog_n_1<29:33> LBL: h31 ARG0: x27 ]  [ udef_q<34:57> LBL: h32 ARG0: x33 [ x PERS: 3 ] RSTR: h34 BODY: h35 ]  [ _and_c<34:37> LBL: h10 ARG0: x5 ARG1: x18 ARG2: x33 ]  [ udef_q<38:48> LBL: h36 ARG0: x37 [ x PERS: 3 NUM: pl IND: + ] RSTR: h38 BODY: h39 ]  [ compound<38:48> LBL: h40 ARG0: e41 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: x37 ARG2: x42 [ x IND: + PT: notpro ] ]  [ udef_q<38:43> LBL: h43 ARG0: x42 RSTR: h44 BODY: h45 ]  [ _chase_n_1<38:43> LBL: h46 ARG0: x42 ]  [ _dog_n_1<44:48> LBL: h40 ARG0: x37 ]  [ udef_q<49:57> LBL: h47 ARG0: x48 [ x PERS: 3 NUM: sg IND: + ] RSTR: h49 BODY: h50 ]  [ _and_c<49:52> LBL: h51 ARG0: x33 ARG1: x37 ARG2: x48 ]  [ _dog_n_1<53:57> LBL: h52 ARG0: x48 ] > HCONS: < h0 qeq h1 h8 qeq h10 h14 qeq h16 h19 qeq h30 h23 qeq h25 h28 qeq h31 h34 qeq h51 h38 qeq h40 h44 qeq h46 h49 qeq h52 > ICONS: < > ]"""
        self.pathological2 = """[ LTOP: h0 INDEX: e2 [ e SF: prop TENSE: pres MOOD: indicative PROG: - PERF: - ] RELS: < [ _dog_v_1<0:4> LBL: h1 ARG0: e4 [ e SF: prop TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: i5 ARG2: x6 [ x PERS: 3 NUM: pl IND: + ] ]  [ _and_c<5:8> LBL: h1 ARG0: e7 [ e SF: prop TENSE: pres MOOD: indicative PROG: - PERF: - ] ARG1: e4 ARG2: e8 [ e SF: prop TENSE: pres MOOD: indicative PROG: - PERF: - ] ]  [ _dog_v_1<9:13> LBL: h1 ARG0: e8 ARG1: i5 ARG2: x6 ]  [ udef_q<14:24> LBL: h9 ARG0: x6 RSTR: h10 BODY: h11 ]  [ compound<14:24> LBL: h12 ARG0: e13 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: x6 ARG2: x14 [ x IND: + PT: notpro ] ]  [ udef_q<14:19> LBL: h15 ARG0: x14 RSTR: h16 BODY: h17 ]  [ _chase_n_1<14:19> LBL: h18 ARG0: x14 ]  [ _dog_n_1<20:24> LBL: h12 ARG0: x6 ]  [ _and_c<25:28> LBL: h1 ARG0: e2 ARG1: e7 ARG2: e19 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ]  [ _dog_v_1<29:32> LBL: h1 ARG0: e20 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ARG1: i21 ARG2: x22 [ x PERS: 3 NUM: pl ] ]  [ _and_c<33:36> LBL: h1 ARG0: e19 ARG1: e20 ARG2: e23 [ e SF: prop TENSE: untensed MOOD: indicative PROG: - PERF: - ] ]  [ _chase_v_1<37:42> LBL: h1 ARG0: e23 ARG1: i21 ARG2: x22 ]  [ udef_q<43:57> LBL: h24 ARG0: x22 RSTR: h25 BODY: h26 ]  [ udef_q<43:47> LBL: h27 ARG0: x28 [ x PERS: 3 NUM: pl IND: + ] RSTR: h29 BODY: h30 ]  [ _dog_n_1<43:47> LBL: h31 ARG0: x28 ]  [ _and_c<48:51> LBL: h32 ARG0: x22 ARG1: x28 ARG2: x33 [ x PERS: 3 NUM: pl IND: + ] ]  [ udef_q<52:57> LBL: h34 ARG0: x33 RSTR: h35 BODY: h36 ]  [ _dog_n_1<52:57> LBL: h37 ARG0: x33 ] > HCONS: < h0 qeq h1 h10 qeq h12 h16 qeq h18 h25 qeq h32 h29 qeq h31 h35 qeq h37 > ICONS: < > ]"""
        self.m1s = (self.m1, self.m1b, self.m1c, self.m1d, self.m1e, self.m1f, self.m1g)
        self.m1_sames = (self.m1, self.m1b, self.m1c, self.m1d, self.m1e, self.m1f, self.m1g)
        self.m2s = (self.m2, self.m2b)
        self.m3s = (self.m3, self.m3b, self.m3c)
        self.pathologicals = (self.pathological1, self.pathological2)
        self.allm = (*self.m1s, *self.m2s, *self.m3s, *self.pathologicals)

    def test_basic_self(self):
        mrs = "[ LTOP: h0 INDEX: e2 [ e SF: prop-or-ques ] RELS: < [ unknown<0:5> LBL: h1 ARG0: e2 ARG: x4 [ x PERS: 3 NUM: sg ] ]  [ udef_q<0:5> LBL: h5 ARG0: x4 RSTR: h6 BODY: h7 ]  [ _hello_n_1<0:5> LBL: h8 ARG0: x4 ] > HCONS: < h0 qeq h1 h6 qeq h8 > ICONS: < > ]"
        actual = compare(mrs, mrs)
        self.assertTrue(actual)

    def test_basic_diff(self):
        hello = "[ LTOP: h0 INDEX: e2 [ e SF: prop-or-ques ] RELS: < [ unknown<0:5> LBL: h1 ARG0: e2 ARG: x4 [ x PERS: 3 NUM: sg ] ]  [ udef_q<0:5> LBL: h5 ARG0: x4 RSTR: h6 BODY: h7 ]  [ _hello_n_1<0:5> LBL: h8 ARG0: x4 ] > HCONS: < h0 qeq h1 h6 qeq h8 > ICONS: < > ]"
        world = "[ LTOP: h0 INDEX: e2 [ e SF: prop-or-ques ] RELS: < [ unknown<0:5> LBL: h1 ARG0: e2 ARG: x4 [ x PERS: 3 NUM: sg IND: + ] ]  [ udef_q<0:5> LBL: h5 ARG0: x4 RSTR: h6 BODY: h7 ]  [ _world_n_of<0:5> LBL: h8 ARG0: x4 ARG1: i9 ] > HCONS: < h0 qeq h1 h6 qeq h8 > ICONS: < > ]"
        actual = compare(hello, world)
        self.assertFalse(actual)

    def test_all_identity(self):
        for mrs in self.allm:
            actual = compare(mrs, mrs)
            self.assertTrue(actual)

    def test_m1(self):
        self.assertFalse(compare(self.m1, self.m1b)) # Note LNK values maybe don't matter?
        self.assertFalse(compare(self.m1, self.m1c))
        self.assertFalse(compare(self.m1, self.m1d))
        self.assertFalse(compare(self.m1, self.m1e))
        self.assertFalse(compare(self.m1, self.m1f))
        self.assertFalse(compare(self.m1, self.m1g))

    def test_m2(self):
        self.assertFalse(compare(self.m2, self.m2b))

    def test_m3(self):
        self.assertTrue(compare(self.m3, self.m3b))
        self.assertTrue(compare(self.m3, self.m3c))
        self.assertTrue(compare(self.m3b, self.m3c))

    def test_pathological(self):
        self.assertFalse(compare(self.pathological1, self.pathological2))

/*
[2018-04-30] Challenge #359 [Easy] Regular Paperfold Sequence Generator
Link to challenge: https://www.reddit.com/r/dailyprogrammer/comments/8g0iil/20180430_challenge_359_easy_regular_paperfold/
 */
public class PaperFold {
    
    private int nCycles;
    private StringBuilder seq;

    PaperFold(int nCycles) {
        this.nCycles = nCycles;
        this.seq = new StringBuilder("1");
    }

    public void calcSeq() {
        calcSeq(nCycles);
    }

    private void calcSeq(int n) {
        if (n == 0)
            return;

        int currentVal = 1;
        for (int i = 0; i <= seq.length(); i += 2) {
            seq.insert(i, currentVal);
            currentVal = 1 - currentVal; // invert
        }

        calcSeq(n - 1);
    }

    public String toString() {
        return seq.toString();
    }

    public static void main(String[] args) {
        PaperFold pFold = new PaperFold(8);
        pFold.calcSeq();
        System.out.println(pFold);
    }
}
#!/usr/bin/python3

import luigi # for Task, Parameter

class FileExists(luigi.Task):
    filename = luigi.Parameter()
    def output(self):
        return luigi.LocalTarget(self.filename)
    def run(self):
        pass

class CountLines(luigi.Task):

    def requires(self):
        """
        What is the input to this task?
        This is an array because there could be many inputs to one task.
        """
        return [FileExists(filename="input.txt")]

    def output(self):
        """
        Where will this Task produce output?
        This is just a single output.
        """
        return luigi.LocalTarget('output.txt')

    def run(self):
        """
        How do I run this Task?
        """
        count=0
        for i in self.input():
            with i.open() as f_in:
                while f_in.readline():
                    count+=1
        with self.output().open("w") as f_out:
            f_out.write(str(count))

#luigi.run()
#luigi.run()
luigi.run(['--local-scheduler','CountLines'])

package io.github.nguyentaijs.command.command;


import io.github.nguyentaijs.command.receiver.CeilingFan;

public class CeilingFanHighCommand implements Command {

	private CeilingFan ceilingFan;

	private CeilingFanHighCommand() {

	}

	public CeilingFanHighCommand(CeilingFan ceilingFan) {
		this.ceilingFan = ceilingFan;
	}

	@Override
	public void execute() {
		ceilingFan.high();

	}

	@Override
	public void undo() {
		ceilingFan.low();
	}
	
}
